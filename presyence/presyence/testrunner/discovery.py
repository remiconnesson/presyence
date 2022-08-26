""" This file is about looking for test files
"""
from pathlib import Path


def discover_test_files(pattern="**/*.spec.sy.py", directory="."):
    p = Path(directory)
    test_files = p.glob(pattern)
    return list(
        test_files
    )  # return a list of files instead of an iterator for convenience
