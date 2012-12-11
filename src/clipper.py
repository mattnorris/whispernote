#!/usr/bin/env python

# Script
import sys
from optparse import OptionParser

# HTML Parsing
import urlparse
from bs4 import BeautifulSoup

# Email 

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.encoders import encode_base64

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
        msg.attach(MIMEText(text))

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
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachmentFilePath))
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

# span.highlight for all highlights
# blockquote for highlights from a single book

def get_all_highlights(filepath): 
    """
    Returns an array of highlight dictionaries: content, link, and generated IDs 
    """
    html_doc = open(filepath, 'r')
    soup = BeautifulSoup(html_doc)

    # Get all of the span elements whose class is "highlight". 
    highlights = soup.find_all('span', 'highlight')
    hdicts = []
    for hl in highlights: 
        # Save the Kindle URI link. 
        klink = hl.nextSibling['href']
        # Remove all the unnecessary attributes (style, etc.) from the link. 
        hl.nextSibling.attrs = {}
        hl.nextSibling['href'] = klink
        # Append the results to the array of highlights. 
        hdicts.append(dict(
            text=hl.string, 
            link=hl.nextSibling.encode('ascii'), 
            id=create_enid(klink)))

    return hdicts

def main(): 
    usage = "usage: %prog [options] highlights.html name@gmail.com gmail_password email@m.evernote.com"
    parser = OptionParser(usage)
    parser.add_option("-d", "--debug", action="store_true", 
        help="Print debug information")
    parser.add_option("-l", "--limit", action="store", type="int", 
        help="Limit the number of highlights processed")
    options, args = parser.parse_args()

    # print 'opts', options
    # print 'args', args

    if options.debug: 
        if len(args) < 1: 
            parser.error("incorrect number of arguments")
    elif len(args) < 4: 
        parser.error("incorrect number of arguments")

    # Create the Mailer to send the emails. 
    mailer = Mailer(args[1], args[2], args[3])

    highlights = get_all_highlights(args[0])
    print 'Found %d highlights. Processing...' % len(highlights)
    for count, highlight in enumerate(highlights): 
        if options.limit is None or count < options.limit: 
            print '\nProcessing highlight %d...' % (count + 1)
            if options.debug: 
                print highlight
            else: 
                mailer.send_mail('Highlight %d' % (count + 1), 
                    highlight['text'])
    print '\nDone.'

if __name__ == '__main__': 
    main()
