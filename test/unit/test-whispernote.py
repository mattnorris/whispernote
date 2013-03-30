#!/usr/bin/env python

"""
Tests whispernote and its supporting functions (e.g., URL parsing). 
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
import whispernote

from lib.bs4 import BeautifulSoup
from urlparse import urlparse

__homepage__ = "http://mattnorris.me"

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

    def test_array_slicing(self): 
        array = ['apples', 'bananas', 'pears', 'oranges', 'peaches']

        self.assertEqual(['apples', 'bananas', 
            'pears', 'oranges', 'peaches'], array[0:])
        # Is original array affected? 
        self.assertEqual(['apples', 'bananas', 
            'pears', 'oranges', 'peaches'], array)
        # Nope. 

        self.assertEqual(['pears', 'oranges', 'peaches'], array[2:])
        self.assertEqual(['peaches'], array[4:])

    # Test the script's functions. 

    def test_create_enid(self): 
        enid = whispernote.create_enid(
            "kindle://book?action=open&asin=B0047O2PXK&location=38")
        self.assertEqual("openB0047O2PXK38", enid)

        enid = whispernote.create_enid(
            "kindle://book?action=open&asin=B004TP29C4&location=4063")
        self.assertEqual('openB004TP29C44063', enid)

    def test_get_all_highlights(self): 
        filepath = os.path.join(INPUT_PATH, 'kindle-highlights.html')
        html_doc = open(filepath, 'r')
        soup = BeautifulSoup(html_doc)
        
        highlights = whispernote.get_all_highlights(soup)
        
        self.assertEqual(153, len(highlights))

        # Get the last highlight to test. 
        last = highlights[-1]

        self.assertFalse(last['book_title'])
        self.assertEqual('thirty-six words, but a hundred assumptions.', 
            last['text'])
        self.assertEqual('<a href="kindle://book?action=open&amp;asin=B002MUAJ2A&amp;location=1700" ' \
            'title="Open this highlight on Kindle">Read&#160;more&#160;at&#160;location&#160;1700</a>', 
            last['link'])
        self.assertEqual('openB002MUAJ2A1700', 
            last['id'])

    def test_get_book_highlights(self): 
        filepath = os.path.join(INPUT_PATH, 'kindle-single-book-sample.html')
        html_doc = open(filepath, 'r')
        soup = BeautifulSoup(html_doc)

        highlights = whispernote.get_highlights(soup)
        
        self.assertEqual(27, len(highlights))
        self.assertEqual('Fairy and Folk Tales of the Irish Peasantry', 
            highlights[0]['book_title'])
        self.assertEqual('openB004TP29C40001', highlights[0]['id'])
        self.assertEqual('<a href="kindle://book?action=open&amp;asin=B004TP29C4&amp;location=1" ' \
            'title="Open this book on Kindle">Open this book on Kindle</a>', 
            highlights[0]['link'])
