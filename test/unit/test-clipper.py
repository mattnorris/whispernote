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

# Import the modules we want to test.
import clipper

__author__="Matthew Norris"

class TestClipper (unittest.TestCase):
    """
    Tests the EFS Project Manager.
    """
    def setUp(self):
        super(TestClipper, self).setUp()

    def tearDown(self):
        super(TestClipper, self).tearDown()

    def test_get_all_highlights(self):
        self.assertFalse(True)