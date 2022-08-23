import pandas as pd
from class_definitions import SimpleSuccessTest, SimpleExceptionTest, TestGroup
from demo_function import identity

tests = []

ok = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
ko = pd.DataFrame({'col1': [1, 2], 'col2': [4, 4]})


tg = TestGroup("The identity function")
tg += SimpleSuccessTest(
    "Must return the same dataframe",
    identity,
    ok,
    ok
)

tg += SimpleSuccessTest(
    "Must return the same but will fail",
    identity,
    ok,
    ko
)

tests += tg
