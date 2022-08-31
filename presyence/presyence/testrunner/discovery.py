""" This file is about looking for test files
"""
from pathlib import Path
import importlib.machinery
import importlib.util
import sys
import types


def discover_test_files(pattern="**/*.spec.sy.py", directory=".") -> list[Path]:
    """ This will discover file matching the specified pattern in the tree starting at the directory.

    Currently we enforce the pattern (ending in .spec.sy.py) and directory (pwd) but this is purely for simplicity.
    """
    p = Path(directory)
    test_files = p.glob(pattern)
    return list(
        test_files
    )  # return a list of files instead of an iterator for convenience


def extract_tests_from_file(file):
    """Will execute the .py file and get the value of the `TESTS` that should be inside.
    """
    # get the true absolute name of the file
    file = file.resolve()
    parent, name = file.parent, file.name
    # add parent to path to help with relative imports 
    if str(parent) not in sys.path:
        sys.path.append(str(parent))
    # in the next lines we will import the file
    module_name = name
    spec = importlib.util.spec_from_file_location(module_name, file)
    # test_module is the .py containing the tests to run 
    test_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = test_module
    spec.loader.exec_module(test_module)
    # check that a lists named TESTS is present
    tests = test_module.__dict__.get("TESTS", [])
    if not tests:
        raise NotImplementedError("Currently, all `.spec.sy.py` must contain a TESTS list containing SimpleTest")
    return tests
