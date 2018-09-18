import pytest
import sys


class TestCreateAccount:
    @pytest.fixture
    def setup_and_destroy(self):
        # setup code
        self.itemList = [1,2,3]

        # destroy code
        yield
        self.itemList = None

    def test_account(self, setup_and_destroy):
        assert self.itemList == [1,2,3]


if __name__ == '__main__':
    pytest.main(sys.argv)
