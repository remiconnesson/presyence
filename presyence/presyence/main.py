import typer
from .testrunner.discovery import discover_test_files

app = typer.Typer()


@app.command()
def main():
    print("Looking for tests")
    test_files = discover_test_files()
    print(test_files)
    if "No test file found":
        typer.Abort()
    if "No tests found in file":
        typer.Abort()
    print("Running tests")
    print("Creating the test report")
    print("Serving the test report on http://localhost:5000/")
