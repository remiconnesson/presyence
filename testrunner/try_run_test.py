import inspect
from class_definitions import TestGroup, SimpleSuccessTest, SimpleExceptionTest, SimpleTest
from demo import tests


def inspect_test(test: SimpleTest):
    print(inspect.getsource(test.function))

def get_df_as_csv(test: SimpleTest):
    print(test.test_input.to_csv(index=False))
    print(test.test_output.to_csv(index=False))


def run_tests(tests: list[TestGroup | SimpleTest]):
    for test in tests:
        if isinstance(test, TestGroup):
            run_tests(test.tests)
        else:
            if isinstance(test, SimpleSuccessTest):
                print("SST", test)
            elif isinstance(test, SimpleExceptionTest):
                print("SET", test)
            inspect_test(test)
            get_df_as_csv(test)


run_tests(tests)
