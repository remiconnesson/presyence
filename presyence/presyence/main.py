import typer
import dataclasses
from .testrunner.discovery import discover_test_files, extract_tests_from_file
from .reporter.server import run_server_and_inject_payload

app = typer.Typer()


@app.command()
def main():
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
    run_server_and_inject_payload(test_report)
