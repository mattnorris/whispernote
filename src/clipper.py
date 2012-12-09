#!/usr/bin/env python

import sys
from optparse import OptionParser
import urlparse
from bs4 import BeautifulSoup

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
            highlight=hl.string, 
            link=hl.nextSibling, 
            id=create_enid(klink)))

    return hdicts

def main(): 
    usage = "usage: %prog [options] highlights.html name@gmail.com gmail_password email@m.evernote.com"
    parser = OptionParser(usage)
    parser.add_option("-d", "--debug", action="store_true", 
        help="Print debug information")
    options, args = parser.parse_args()

    # print 'opts', options
    # print 'args', args

    if options.debug: 
        if len(args) < 1: 
            parser.error("incorrect number of arguments")
    elif len(args) < 4: 
        parser.error("incorrect number of arguments")

    highlights = get_all_highlights(args[0])
    for h in highlights: 
        print h

if __name__ == '__main__': 
    main()
