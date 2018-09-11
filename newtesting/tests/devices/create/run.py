#!/usr/bin/env python

import os,sys,inspect
import glob
import re

# This is used for building the path to the helpers folder.
# As the tests and helpers are located in seperate folders we need to add 
# the helpers to the sys.path so that we can import them correctly.
def buildImportPath():
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    sys.path.insert(0,(re.search(r'.*newtesting\\',current_dir)).group(0) + "helpers")

def getTestList():
    unfilteredList = [fn for fn in glob.glob("**/*.py",recursive=True) if not fn.endswith("run.py")]
    print(unfilteredList)

if __name__ == "__main__":
    buildImportPath()
    getTestList()