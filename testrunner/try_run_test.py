import inspect
from class_definitions import TestGroup, SimpleSuccessTest, SimpleExceptionTest, SimpleTest
from demo import tests


def inspect_test(test: SimpleTest):
    print(inspect.getsource(test.function))


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


run_tests(tests)