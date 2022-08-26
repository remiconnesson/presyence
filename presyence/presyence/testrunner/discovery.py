""" This file is about looking for test files
"""
from pathlib import Path
import importlib.machinery
import types


def discover_test_files(pattern="**/*.spec.sy.py", directory="."):
    p = Path(directory)
    test_files = p.glob(pattern)
    return list(
        test_files
    )  # return a list of files instead of an iterator for convenience


def extract_tests_from_file(file, module_name="testmodule"):
    loader = importlib.machinery.SourceFileLoader(module_name, str(file))
    testmodule = types.ModuleType(module_name)
    loader.exec_module(testmodule)
    # check that a lists named TESTS is present
    tests = testmodule.__dict__.get("TESTS", [])
    return tests
