#!/bin/bash
# build
#
# Zips this project for distribution, including all dependent libraries. 
#
cd ../output
cp -ar ../src ./whispernote 
zip -r9 --exclude=*.pyc* whispernote.zip whispernote
rm -fr whispernote
