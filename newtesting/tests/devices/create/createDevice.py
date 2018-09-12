#!/usr/bin/env python

import run
import resthelper

# Put your pre-test setup in here(creating objects, setting navigation url, etc...)
def setup():
   resthelper.resthelperFunc()

# Put your deconstruction in here
def destroy():
    pass

# Put the test itself in here
def test():
    print("running test create")









#helper function for the run.py
def runTest():
    setup()
    test()
    destroy()

if __name__ == "__main__":
    setup()
    runTest()
