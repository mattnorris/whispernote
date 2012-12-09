#!/usr/bin/env python
"""
Tests the web page Clipper. 
"""

import unittest
import os
import sys
import shutil

# Get the relevant paths of the modules and tests.
CURR_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.normpath(os.path.join(CURR_PATH, '../../src/'))
OUTPUT_PATH = os.path.normpath(os.path.join(CURR_PATH, '../output'))
INPUT_PATH = os.path.normpath(os.path.join(CURR_PATH, '../input'))

# Update the system path so we can find the modules we want to test.
sys.path.append(MODULE_PATH)

# Import the modules and functions we wish to test.
import clipper

from bs4 import BeautifulSoup
from urlparse import urlparse

__author__="Matthew Norris"

class TestBeautifulSoup (unittest.TestCase):
    def setUp(self):
        super(TestBeautifulSoup, self).setUp()

    def tearDown(self):
        super(TestBeautifulSoup, self).tearDown()

    def test_beautiful_soup(self):
        # Get the sample HTML. 
        filepath = os.path.join(INPUT_PATH, 'kindle-highlights.html')
        html_doc = open(filepath, 'r')

        soup = BeautifulSoup(html_doc)

        self.assertEqual('title', soup.title.name)
        # soup.title returns an object: <title>Amazon Kindle: Your Highlights</title>

        self.assertEqual('Amazon Kindle: Your Highlights', soup.title.string)
        #self.assertEqual('head', soup.title.parent.name)

        # Get all of the span elements whose class is "highlight". 
        highlights = soup.find_all('span', 'highlight')
        self.assertTrue(150 < len(highlights))

        # Verify the first. 
        h = highlights[0]
        self.assertEqual('when no longer worshipped and fed with offerings, dwindled away in the popular imagination, and now are only a few spans high."', 
            h.string)
        # Get the link next to it. 
        h_link = h.nextSibling
        self.assertEqual("<class 'bs4.element.Tag'>", str(h_link.__class__))
        self.assertEqual("Tag", h_link.__class__.__name__)

    def test_urlparse(self): 
        link1 = "kindle://book?action=open&asin=B004TP29C4&location=4063"
        parts = urlparse(link1)
        self.assertEqual('?action=open&asin=B004TP29C4&location=4063', 
            parts.path)
        # Create a highlight ID from the URL path. 
        hid = ''.join([param.split('=')[1] for param in parts.path.split('&')])
        self.assertEqual('openB004TP29C44063', hid)

    # Test the script's functions. 

    def test_create_enid(self): 
        enid = clipper.create_enid(
            "kindle://book?action=open&asin=B0047O2PXK&location=38")
        self.assertEqual("openB0047O2PXK38", enid)

        enid = clipper.create_enid(
            "kindle://book?action=open&asin=B004TP29C4&location=4063")
        self.assertEqual('openB004TP29C44063', enid)

    def test_get_all_highlights(self): 
        html_doc = os.path.join(INPUT_PATH, 'kindle-highlights.html')
        highlights = clipper.get_all_highlights(html_doc)
        self.assertEqual(153, len(highlights))
