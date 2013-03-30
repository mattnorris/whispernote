#!/usr/bin/env python

"""
Creates Evernote notes for all of your Kindle highlights. 
"""

# Script
import sys
from optparse import OptionParser
import datetime

# HTML Parsing
import urlparse
from lib.bs4 import BeautifulSoup

# Email 
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.encoders import encode_base64

__homepage__ = "http://mattnorris.me"

# Generic link if we can't find the exact highlight position. 
LINK = '<a href="kindle://book?action=open&amp;asin=%s&amp;location=1" ' \
    'title="Open this book on Kindle">Open this book on Kindle</a>'

class Mailer: 

    def __init__(self, gmailUser, gmailPassword, recipient): 
        self.gmailUser = gmailUser
        self.gmailPassword = gmailPassword
        self.recipient = recipient

    def send_mail(self, subject, text, *attachmentFilePaths):
        """
        Sends an email with the specified subject, body, and attachments.
        """
        msg = MIMEMultipart()
        msg['From'] = self.gmailUser
        msg['To'] = self.recipient
        msg['Subject'] = subject
        # For plain text. 
        # msg.attach(MIMEText(text))
        # For HTML emails with UTF characters. 
        msg.attach(MIMEText(text.encode('utf-8'), 'html'))

        for attachmentFilePath in attachmentFilePaths:
            msg.attach(self._get_attachment(attachmentFilePath))

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.gmailUser, self.gmailPassword)
        mailServer.sendmail(self.gmailUser, self.recipient, msg.as_string())
        mailServer.close()

        print('Sent email to %s.' % self.recipient)

    def _get_attachment(self, attachmentFilePath):
        """
        Formats the file on the given path and assigns the proper MIME type.
        """
        contentType, encoding = mimetypes.guess_type(attachmentFilePath)

        if contentType is None or encoding is not None:
            contentType = 'application/octet-stream'
        mainType, subType = contentType.split('/', 1)
        file = open(attachmentFilePath, 'rb')

        if mainType == 'text':
            attachment = MIMEText(file.read())
        elif mainType == 'message':
            attachment = email.message_from_file(file)
        elif mainType == 'image':
            attachment = MIMEImage(file.read(), _subType=subType)
        elif mainType == 'audio':
            attachment = MIMEAudio(file.read(), _subType=subType)
        else:
            attachment = MIMEBase(mainType, subType)
            attachment.set_payload(file.read())
            encode_base64(attachment)

        file.close()
        attachment.add_header('Content-Disposition', 'attachment', 
            filename=os.path.basename(attachmentFilePath))
        return attachment

def create_enid(huri): 
    """
    Creates an Evernote unique ID based on the highlight's URI. 
    A Kindle highlight is composed of a 'asin', or ISBN of the book, 
    and a location. 

    huri - highlight URI

    kindle://book?action=open&asin=B004TP29C4&location=4063

    will return...

    openB004TP29C44063
    """
    return ''.join([param.split('=')[1] \
        for param in urlparse.urlparse(huri).path.split('&')])

def get_all_highlights(soup): 
    """
    Returns an array of highlight dictionaries - content, link, 
    and generated IDs - for all books. 
    """
    # Get all of the span elements whose class is "highlight". 
    highlights = soup.find_all('span', 'highlight')

    # TODO: If HTML is not found, then we are using My Clippings.txt. 

    hdicts = []
    for highlight in highlights: 
        # Save the Kindle URI link. 
        klink = highlight.nextSibling['href']
        # Remove all the unnecessary attributes (style, etc.) from the link. 
        highlight.nextSibling.attrs = {}
        highlight.nextSibling['href'] = klink
        highlight.nextSibling['title'] = "Open this highlight on Kindle"
        
        # TODO: Get ASIN (ISBN) for book_title.
        book_title = ''

        # Append the results to the array of highlights. 
        hdicts.append(dict(
            book_title=book_title, 
            text=highlight.string, 
            link=highlight.nextSibling.encode('ascii'), 
            id=create_enid(klink)
            ))

    return hdicts

def get_highlights(soup): 
    """
    Returns an array of highlight dictionaries - content, link, 
    and generated IDs - for a single book. 
    """
    book_title = soup.title.string.replace("Amazon Kindle: ", "").strip()
    book_isbn = soup.select('input[name="asin"]')[0]['value']
    highlights = soup.find_all('blockquote')
    hdicts = []
    for count, highlight in enumerate(highlights): 
        hdicts.append(dict(
            book_title=book_title, 
            text=highlight.string, 
            link=LINK % book_isbn, 
            id='open' + book_isbn + '{0:04d}'.format(count + 1)
            ))

    return hdicts

def main(): 
    usage = "usage: %prog [options] highlights.html name@gmail.com gmail_password email@m.evernote.com"
    parser = OptionParser(usage)
    parser.add_option("-d", "--debug", action="store_true", 
        help="Print debug information")
    parser.add_option("-l", "--limit", action="store", type="int", 
        help="Limit the number of highlights processed")
    parser.add_option("-s", "--start", action="store", type="int", 
        help="Starts processing highlights at the given position.")
    options, args = parser.parse_args()

    if options.debug: 
        if len(args) < 1: 
            parser.error("incorrect number of arguments")
    elif len(args) < 4: 
        parser.error("incorrect number of arguments")

    # Create the Mailer to send the emails. 
    try: 
        mailer = Mailer(args[1], args[2], args[3])
    except IndexError: 
        parser.error("incorrect number of arguments")

    BODY = """
    <p>%s</p>
    <p><em>%s</em></p>
    <p>%s</p>
    <hr/>
    <p>Use these unique IDs to search for duplicate notes in Evernote.</p>
    <ul>
    <li><em>Highlight ID:</em> %s</li>
    <li><em>Batch ID:</em> %s</li>
    </ul>
    """
    now = datetime.datetime.now()

    html_doc = open(args[0], 'r')
    soup = BeautifulSoup(html_doc)

    highlights = []
    if soup.title.string == 'Amazon Kindle: Your Highlights': 
        highlights = get_all_highlights(soup)
    else: 
        highlights = get_highlights(soup)

    print 'Found %d highlights.' % len(highlights)

    # Start at the starting point, if one is given. 
    start = options.start - 1 if options.start else 0
    # Process. 
    for count, highlight in enumerate(highlights[start:]): 
        
        if options.limit is None or count < options.limit: 
            title = 'Highlight %d clipped on %s' % \
                    (start + 1, now.strftime("%B %d, %Y at %I:%M %p"))
            
            body = BODY % \
                    (highlight['text'], 
                        highlight['book_title'], 
                        highlight['link'], 
                        highlight['id'], 
                        now.strftime("batch%Y%m%d%H%M%S"))

            print '\nProcessing: %s...' % title

            if options.debug: 
                print BeautifulSoup(body).prettify()
            else: 
                mailer.send_mail(title + ' #kindle #highlight', body)

        start += 1 

    print '\nDone.'

if __name__ == '__main__': 
    main()
