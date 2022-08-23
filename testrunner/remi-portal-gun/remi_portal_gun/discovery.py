import importlib.machinery
import types
from inspect import getmembers, isfunction
# I need to find all files that contain tests
from pathlib import Path

def discovery():
    p = Path('.')

    test_files = list(p.glob('**/*.spec.sy.py'))
    # then load them up dynamically

    each_module_tests = []

    if not test_files:
        print("NO TEST FILES YO")
    else:
        for i, test_file in enumerate(test_files):
            module_name = "test_modules_{i}"
            loader = importlib.machinery.SourceFileLoader(module_name, str(test_file))
            m = types.ModuleType(module_name)
            loader.exec_module(m)
            # then for each check if there's a test list
            tests = m.__dict__.get("TESTS", "notfound")
            if tests=="notfound":
                raise Exception("Your test files must contain a TESTS variable, which is a list of SimpleTest")
            # then make a list of list of tests
            each_module_tests.append(tests)

        print(each_module_tests)






