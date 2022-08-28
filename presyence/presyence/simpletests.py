from dataclasses import dataclass, field
from collections.abc import Callable
from abc import ABC, abstractmethod
import pandas as pd
import traceback
import inspect

@dataclass
class SimpleTestExport:
    title: str
    function: str
    input: str
    expected_output: str


@dataclass
class SimpleTest:
    title: str
    function: Callable
    input: pd.DataFrame | pd.Series
    expected_output: pd.DataFrame | pd.Series

    def export(self):
        return SimpleTestExport(
            title=self.title,
            function=inspect.getsource(self.function),
            input=self.input.to_csv(index=False),
            expected_output=self.expected_output.to_csv(index=False)
        )

    def __radd__(self, tests: list):
        if isinstance(tests, list):
            tests.append(self)
            return tests
        else:
            raise TypeError(
                (
                    "presyence SimpleTest can only be added to a list, "
                    f"found:, {type(tests)}"
                )
            )

    def run(self):
        try:
            testrun_output = self.function(self.input)
            if isinstance(self.expected_output, pd.DataFrame):
                assert_same = pd.testing.assert_frame_equal
            elif isinstance(self.expected_output, pd.Series):
                assert_same = pd.testing.assert_serie_equal
            else:
                raise NotImplementedError("Expected output must be a pandas DataFrame or a Serie")
            if not isinstance(testrun_output, pd.DataFrame | pd.Series):
                raise NotImplementedError
            assert_same(self.expected_output, testrun_output)
        except NotImplementedError:
            raise
        except AssertionError as e:
            result = WrongResult(
                testrun_output = testrun_output.to_csv(index=False),
                assertion_error_message = e.args[0]
            )
        except Exception:
            result = Crash(
                traceback = traceback.format_exc()
            )
        else:
            result = Success()
        finally:
            return SimpleTestReport(
                test = self.export(),
                result = result
            )


@dataclass
class TestResult(ABC):
    successful: bool = field(init=False)
    status: str = field(init=False)

    @abstractmethod
    def __bool__(self):
        ...

    def __post_init__(self):
        self.successful = bool(self)
        self.status = self.__class__.__name__


@dataclass
class Success(TestResult):
    def __bool__(self):
        return True

@dataclass
class WrongResult(TestResult):
    testrun_output: str
    assertion_error_message: str
    def __bool__(self):
        return False

@dataclass
class Crash(TestResult):
    traceback: str
    def __bool__(self):
        return False

@dataclass
class SimpleTestReport:
    test: SimpleTestExport
    result: TestResult
