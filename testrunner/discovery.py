# I need to find all files that contain tests
from pathlib import Path

p = Path('.')

print(list(p.glob('**/*.spec.sy.py')))



# then load them up dynamically

# then for each check if there's a test list

# then make a list of list of tests

