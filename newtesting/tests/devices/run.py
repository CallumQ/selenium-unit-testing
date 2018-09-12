#!/usr/bin/env python

import os,sys,inspect
import importlib
import glob
import re

# This is used for building the path to the helpers folder.
# As the tests and helpers are located in seperate folders we need to add 
# the helpers to the sys.path so that we can import them correctly.
def build_helper_imports():
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    sys.path.insert(0,(re.search(r'.*newtesting\\',current_dir)).group(0) + "helpers")

def get_test_list():
    return [fn for fn in glob.glob("**/*.py",recursive=True) if not fn.endswith("run.py")]

# Converts the file paths into imports
def build_test_imports(test_list):
    import_list = []
    for item in test_list:
        parsed_import = item.replace("\\",".").replace(".py","")
        testing = importlib.import_module(parsed_import)
        import_list.append(testing)
    return import_list

def run_tests(tests):
    for test in tests:
        test.runTest()


# if script is called directly, build a list of test files in the current directory and below
if __name__ == "__main__":
    build_helper_imports()
    run_tests(build_test_imports(get_test_list()))
    

#else if the script is import, only set up the imports
elif __name__ == "run":
    build_helper_imports()