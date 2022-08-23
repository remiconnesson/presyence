from class_definitions import TestGroup, SimpleSuccessTest, SimpleExceptionTest
from demo import tests


def run_tests(tests):
    for test in tests:
        if isinstance(test, TestGroup):
            run_tests(test.tests)
        if isinstance(test, SimpleSuccessTest):
            print("SST", test)
        elif isinstance(test, SimpleExceptionTest):
            print("SET", test)


run_tests(tests)
