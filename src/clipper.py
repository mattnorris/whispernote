#!/usr/bin/env python

import sys
from optparse import OptionParser
import urlparse

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

def main(): 
	parser = OptionParser()
	args = sys.argv[1:3]
	if len(args) < 2: 
		parser.error('%s requires 2 arguments.' % sys.argv[0])

	print 'sys.argv', sys.argv

if __name__ == '__main__': 
	main()
