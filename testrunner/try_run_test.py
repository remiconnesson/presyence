import pandas as pd
import traceback
import inspect
from class_definitions import TestGroup, SimpleSuccessTest, SimpleExceptionTest, SimpleTest
from demo import tests


def inspect_test(test: SimpleTest):
    print(inspect.getsource(test.function))

def get_df_as_csv(test: SimpleTest):
    print(test.test_input.to_csv(index=False))
    print(test.test_output.to_csv(index=False))

def exec_test(test: SimpleTest):
    try:
        result = test.function(test.test_input)
        type_of_output = type(test.test_output)
        type_of_result = type(result)
        if type_of_output is not type_of_result:
            raise TypeError(f"Mismatched type {type_of_output} != {type_of_result}")
        if isinstance(result, pd.DataFrame):
            assert_same = pd.testing.assert_frame_equal
        elif isinstance(result, pd.Series):
            assert_same = pd.testing.assert_serie_equal
        else:
            raise NotImplementedError
        test_ok = assert_same(test.test_output, result)
    except AssertionError as e:
        pass
        # the function returned but not with the good value
        # so this is a failing test, and the report will print the result
    except TypeError as e:
        pass
        # the function returned but not with the good value
        # so this is a failing test, and the report will print the result
    except Exception as e:
        # here will need the traceback as a result
        print("START TRACEBACK")
        tb = traceback.format_exc()
        print(tb)
        print("END TRACEBACK")
    else:
        pass
        # the test was successful
        #
    finally:
        print('wrap up')


def run_tests(tests: list[TestGroup | SimpleTest]):
    for test in tests:
        if isinstance(test, TestGroup):
            run_tests(test.tests)
        else:
            if isinstance(test, SimpleSuccessTest):
                pass # print("SST", test)
            elif isinstance(test, SimpleExceptionTest):
                pass # print("SET", test)
            # inspect_test(test)
            # get_df_as_csv(test)
            exec_test(test)


run_tests(tests)

crash_test = SimpleSuccessTest(
    "this must crash",
    lambda  x : 1 / 0,
    False,
    False
)

exec_test(crash_test)
