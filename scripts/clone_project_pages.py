#!/usr/bin/env python

"""
Clones the GitHub Pages of the Whispernote project into a given directory. 
Shortens the development life cycle of new project pages by reusing 
the Whispernote pages. 
"""

from optparse import OptionParser
import tempfile
import distutils.core
from subprocess import call
import os
import shutil

REPO = 'git://github.com/mattnorris/whispernote.git'
REPO_ROOT = 'whispernote'
BRANCH = 'gh-pages'

CSS_DIR = 'assets/css'
BS_REPO = 'git://github.com/twitter/bootstrap.git'

def clone(dest):
    """
    - Clone Whispernote
    - Copy its contents into the desired project
    - Navigate to lib folder and clone bootstrap project into it
    - Move cloned variables.less and bootstrap.less
    """
    # Clone into a temporary directory. 
    clonedir = tempfile.mkdtemp()
    call(['git', 'clone', '-b', BRANCH, REPO, clonedir])

    # Copy the cloned contents, except for the git history. 
    shutil.rmtree(os.path.join(clonedir, '.git'))
    distutils.dir_util.copy_tree(clonedir, dest)

    # Clone the Twitter Bootstrap project. 
    bs_dir = os.path.normpath(os.path.join(dest, 'lib', 'bootstrap'))
    shutil.rmtree(bs_dir)
    call(['git', 'clone', BS_REPO, bs_dir])

    # Move and rename variables.less and bootstrap.less
    css_dir = os.path.normpath(os.path.join(dest, 'assets', 'css'))
    shutil.move(os.path.join(bs_dir, 'less', 'bootstrap.less'), 
        os.path.join(css_dir, 'bootstrap.less.cloned'))
    shutil.move(os.path.join(bs_dir, 'less', 'variables.less'), 
        os.path.join(css_dir, 'variables.less.cloned'))

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