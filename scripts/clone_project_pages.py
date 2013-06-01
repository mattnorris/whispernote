#!/usr/bin/env python

"""
Clones the GitHub Pages of the Whispernote project into a given directory. 
This is meant to shorten the development cycle of the new project page by 
copy/pasting the Whispernote one. 
"""

from optparse import OptionParser
import tempfile
import distutils.core
from subprocess import call
import os

REPO = 'git://github.com/mattnorris/whispernote.git'
REPO_ROOT = 'whispernote'
BRANCH = 'gh-pages'

CSS_DIR = 'assets/css'
BS_DIR = 'lib'

def clone(dest):
    """
    - Clone Whispernote
    - Copy its contents into the desired project
    - Backup variables.less and bootstrap.less -> .bak (they will be overwritten later)
    - Navigate to lib folder and clone bootstrap project into it
    - Move variables.less and bootstrap.less
    """
    # Clone into a temporary directory. 
    clonedir = tempfile.mkdtemp()
    # git clone -b gh-pages git://github.com/mattnorris/whispernote.git DIR
    call(['git', 'clone', '-b', BRANCH, REPO, clonedir])

    # Copy the cloned contents. 
    distutils.dir_util.copy_tree(clonedir, dest)

    # Back up the files bootstrap.less and variables.less for reference.  
    # They will be overwritten momentarily. 
    os.rename(os.path.join(dest, CSS_DIR, 'bootstrap.less'), 
        os.path.join(dest, CSS_DIR, 'bootstrap.less.bak'))
    os.rename(os.path.join(dest, CSS_DIR, 'variables.less'), 
        os.path.join(dest, CSS_DIR, 'variables.less.bak'))

    # Clone the Twitter Bootstrap project. 
    

def main(): 
    usage = "%prog DIR"
    parser = OptionParser(usage)
    options, args = parser.parse_args()

    try: 
        dest = args[0]
    except IndexError: 
        parser.error("requires a directory")
    
    clone(dest)

if __name__ == '__main__': 
    main()