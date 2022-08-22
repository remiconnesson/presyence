from dataclasses import dataclass, field
from collections.abc import Callable
import pandas as pd

@dataclass
class SimpleTest:
    title: str
    function: Callable
    test_input: pd.DataFrame | pd.Series

    def __radd__(self, tests: list):
        if not isinstance(tests, list):
            raise TypeError("presyence SimpleTest expect to be added only to a list or a TestGroup, found:", type(tests))
        tests.append(self)
        return tests

@dataclass
class SimpleSuccessTest(SimpleTest):
    test_output: pd.DataFrame | pd.Series

@dataclass
class SimpleExceptionTest(SimpleTest):
    expected_exception: Exception
    expected_message: str

@dataclass
class TestGroup:
    title: str
    tests: list[SimpleSuccessTest | SimpleExceptionTest] = field(default_factory=list)

    def __iadd__(self, test: SimpleSuccessTest | SimpleExceptionTest):
        self.tests += [test]
        return self

    def __radd__(self, tests: list):
        if not isinstance(tests, list):
            raise TypeError("presyence TestGroup expects to be added only to a list, found:", type(tests))
        tests.append(self)
        return tests
