from dataclasses import dataclass
from collections.abc import Callable
import pandas as pd


@dataclass
class SimpleTest:
    title: str
    function: Callable
    input: pd.DataFrame | pd.Series
    output: pd.DataFrame | pd.Series

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
