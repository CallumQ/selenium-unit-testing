from abc import ABC, abstractmethod
from selenium import webdriver


class BaseTest(ABC):
    # BaseTest is an abstract class to ensure that all tests implement the right functions.
    # an underscore preceding a function denotes that it is private.
    # Do not call these functions directly.
    def __init__(self):
        super().__init__()

    def __init__(self, driver):
        self.driver = driver

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\Callum\Desktop\tests\selenium\helpers\chromedriver.exe")

    # Call this function in your individual test files.
    def run_test(self):
        self._setup()
        self._test()
        self._destroy()

    @abstractmethod
    def _setup(self):
        pass

    @abstractmethod
    def _test(self):
        pass

    @abstractmethod
    def _destroy(self):
        pass
