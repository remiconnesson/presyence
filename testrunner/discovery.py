import importlib.machinery
import types
from inspect import getmembers, isfunction
# I need to find all files that contain tests
from pathlib import Path

p = Path('.')

test_files = list(p.glob('**/*.spec.sy.py'))
# then load them up dynamically

for i, test_file in enumerate(test_files):
    module_name = "test_modules_{i}"
    loader = importlib.machinery.SourceFileLoader(module_name, str(test_file))
    m = types.ModuleType(module_name)
    loader.exec_module(m)
    break
    # then for each check if there's a test list
    # then make a list of list of tests







