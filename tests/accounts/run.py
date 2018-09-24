
import os, sys, inspect
import pytest
import re


def build_helper_imports():
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    sys.path.insert(0, (re.search(r'.*tests\\', current_dir)).group(0) + "helpers")
    print(sys.path)

if __name__ == '__main__':
    build_helper_imports()
    pytest.main()
else:
    build_helper_imports() 