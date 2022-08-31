import typer
import dataclasses
from .testrunner.discovery import discover_test_files, extract_tests_from_file
from .reporter.server import run_server_and_inject_payload

app = typer.Typer()


@app.command()
def main():
    """The only command of the package, will run tests and then report.

    This is how it operates:

    1. It starts to look for presyence test files in the current working directory tree, where the `presyence` command is run.

    Note: presyence test files are python files for which the name ends with `spec.sy.py`.
    2. If it hasn't found any matching file, it will exit.
    3. Then it will dynamically load each matching file, attempting to extract tests from it.
    4. Tests must be stored in a variable called TESTS which is a list of `presyence.simpletests.SimpleTest`
    5. If any matching file fails to declare a TESTS variable, the program will abort.
    6. Each lists of SimpleTest will be concatenated to create a big 1D list of SimpleTest.
    7. Then each SimpleTest will be executed by calling the `SimpleTest.run(self)` method, the result of that operation will be a SimpleTestReport, appendended to a big 1D list of test results.
    8. The list of SimpleTestReport will be added to a dictionary, this dictionary will later be converted to JSON and injected into the frontend code by the local server serving the UI.
    9. We launch the local UI server and we provide it with the dictionary payload, this payload will later be unpacked and formated by the Vue.JS frontend code server from this local server.
    10. To quit serving the user need to hit Ctrl-C.
    """
    print("Looking for tests")
    test_files = discover_test_files()
    print(test_files)
    if not test_files:
        print("No test file found. Test file names must end with '.spec.sy.py'")
        exit()
    tests = []
    for test_file in test_files:
        _tests = extract_tests_from_file(test_file)
        if not _tests:
            print(f"No tests found in file {test_file.absolute()}")
            exit()
        tests += _tests
    print("Running tests")
    test_results = []
    for test in tests:
        test_results += [test.run()]
    print("Creating the test report")
    test_report = {"testReport": test_results}
    print("Serving the test report on http://localhost:5000/")
    print("Hit Ctrl-C to quit.")
    run_server_and_inject_payload(test_report)
