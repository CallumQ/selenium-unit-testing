#!/usr/bin/env python3

from helpers.base_test import BaseTest as AbstractBaseTest
import helpers.rest_helper as RestHelper
import helpers.element_helper as ElementHelper
import sys


class Tester(AbstractBaseTest):

    def _setup(self):
        # Put any of your required setup in here (creating an object, navigating to a specific link, etc...)
        print("setup")

    def _test(self):
        # Put the test itself in here (asserts, performing operations)
        self.driver.get("https://google.co.uk")

    def _destroy(self):
        # Put any clean up steps in here (deleting objects, resetting the webdriver)
        print("destroy")


# support function, used within the run.py to kick off a test
def run_test():
    Tester().run_test()


if __name__ == "__main__":
    run_test()
