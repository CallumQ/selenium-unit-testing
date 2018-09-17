#!/usr/bin/env python3
import glob
import importlib


# recursively gets all .py files in the current directory and subdirectories
def get_test_list():
    return [file for file in glob.glob("**/*.py",recursive=True) if not file.endswith("run.py")]


# Converts the file paths into imports
def build_test_imports(test_list):
    import_list = []

    for item in test_list:
        # converts the slashes in a file path and removes the .py
        # so that the string can then be used to import that file
        # Example this\is\a\test.py becomes this.is.a.test
        parsed_import = item.replace("\\", ".").replace(".py", "")
        # dynamically imports the given string
        testing = importlib.import_module(parsed_import)
        import_list.append(testing)

    return import_list


def run_tests(tests):
    for test in tests:
        test.run_test()


# if script is called directly, build a list of test files in the current directory and below
if __name__ == "__main__":
    run_tests(build_test_imports(get_test_list()))
