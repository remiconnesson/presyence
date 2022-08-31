from dataclasses import dataclass, field, asdict
from collections.abc import Callable
from abc import ABC, abstractmethod
import pandas as pd
import traceback
import inspect


@dataclass
class SimpleTestExport:
    """A stringified representation of a presyence test. Input and Ouputs are representing `.csv`, function is representing valid python code."""

    title: str
    function: str  # supposed to be python code
    input: str  # supposed to be .csv
    expected_output: str  # supposed to be .csv


@dataclass
class TestResult(ABC):
    successful: bool = field(init=False)
    status: str = field(init=False)

    @abstractmethod
    def __bool__(self):
        """test considered success must return True, failed test must return False."""
        ...

    def __post_init__(self):
        """The children will infer it's property from it's classname and it's boolean value."""
        self.successful = bool(self)
        self.status = self.__class__.__name__


@dataclass
class SimpleTestReport:
    """Contains the test statement as well as its outcome formatted in a way serializable to JSON with dataclasses.asdict() function.

    This is what is passed to the frontend UI.
    """

    test: SimpleTestExport
    result: TestResult


@dataclass
class Success(TestResult):
    """The absence of details means absolute success.

    We can envision a SuccessButWithWarning class that have a warning property, yet evaluate to True, as all success should.
    """

    def __bool__(self):
        return True


@dataclass
class WrongResult(TestResult):
    """A wrong result is caracterized by an output different than what was expected, as well as the assertion error message.

    The pandas DataFrame equality assertion function returns somewhat useful error messaged that would be a shame to not pass forward to the UI.
    """

    testrun_output: str
    assertion_error_message: str

    def __bool__(self):
        return False


@dataclass
class Crash(TestResult):
    """A crash is caracterized by a Traceback of what went wrong."""

    traceback: str

    def __bool__(self):
        return False


@dataclass
class SimpleTest:
    """Define a simple test that takes a function and two dataframes, as well as a title.

    The idea is that if `function(input) === expected_output` then the test is a success, otherwise, it's a failure.

    Currently `presyence` only accepts pd.DataFrame, but accepting pd.Series is doable.
    """

    title: str
    function: Callable
    input: pd.DataFrame  # | pd.Series
    expected_output: pd.DataFrame  # | pd.Series

    def __post_init__(self):
        """
        Enforces correct typing.
        """
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`"
                )

    def export(self) -> SimpleTestExport:
        """This method transforms every component of a SimpleTest into strings"""
        return SimpleTestExport(
            title=self.title,
            function=inspect.getsource(self.function),
            input=self.input.to_csv(index=False),
            expected_output=self.expected_output.to_csv(index=False),
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

    def run(self) -> SimpleTestReport:
        """Run the test to create a SimpleTestReport

        This method plan is to:
        1. attempt to run the test
        2. triage exceptions based on (a.) implementation (b.) assertion error (wrong result) (c.) crash during the test
        3. A test result can only be of three valid status (a.) it's a success, (b.) the output is not the one expected, (c.) the function under tests crashed.
        4. Each of this valid status will create a different type of report, requiring different arguments.
        5. Once a test has been ran, we serialize the test to string as well as its outcome. We return both in a SimpleTestReport
        """
        try:
            testrun_output = self.function(self.input)
            if isinstance(self.expected_output, pd.DataFrame):
                assert_same = pd.testing.assert_frame_equal
            elif isinstance(self.expected_output, pd.Series):
                raise NotImplementedError(
                    "pd.Series handling will come in a later version."
                )
                # assert_same = pd.testing.assert_series_equal
            else:
                raise NotImplementedError(
                    "Expected output must be a pandas DataFrame or a Serie"
                )
            if not isinstance(testrun_output, pd.DataFrame | pd.Series):
                raise NotImplementedError
            assert_same(self.expected_output, testrun_output)
        except NotImplementedError:
            # We let NotImplementedError bubble up and crash the program
            raise
        except AssertionError as e:
            result = WrongResult(
                testrun_output=testrun_output.to_csv(index=False),
                assertion_error_message=e.args[
                    0
                ],  # Pandas provide useful error messages so we pass them on to the UI
            )
        except Exception:
            result = Crash(traceback=traceback.format_exc())
        else:
            # absence of Exception means the test was successful
            result = Success()
        finally:
            _test_result = SimpleTestReport(
                test=self.export(),  # the test statement, exported to string
                result=result,  # the test outcome
            )
            return asdict(_test_result)
