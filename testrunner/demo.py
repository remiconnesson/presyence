from class_definitions import SimpleSuccessTest, SimpleExceptionTest, TestGroup

tests = []

tg = TestGroup("The blabla function")
tg += SimpleSuccessTest(1,2,3,4)
tg += SimpleSuccessTest(5,6,7,8)

tests += tg

tests += SimpleExceptionTest(1,2,3,4,5)  

print(tests)



