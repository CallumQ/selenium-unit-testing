import pytest
import sys
import run
from helpers import rest_helper as restHelper
from selenium import webdriver
class TestCreateAccount:
    @pytest.fixture
    def setup_and_destroy(self):
        # setup code
        self.driver = webdriver.Chrome(r"C:\Users\Callum\Downloads\chromedriver.exe")
        restHelper.create_person()
        self.driver.get("https://github.com/")
        # destroy code
        yield
        self.itemList = None
        self.driver.quit()
    def test_account(self, setup_and_destroy):
        assert self.driver.title == "The world’s leading software development platform · GitHub"


if __name__ == '__main__':
    pytest.main(sys.argv)
