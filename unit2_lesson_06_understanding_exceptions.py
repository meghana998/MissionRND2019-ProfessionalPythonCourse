__author__ = 'Kalyan'

notes = """
Exceptions are the default runtime error reporting mechanism in python.

Most modern languages like c#, java have a similar exception model, so your
understanding will carry forward if you end up learning those languages.

Read this to before you start: https://docs.python.org/3/tutorial/errors.html
"""

from placeholders import *

# play with this method to understand the basic exception flow and understand how to follow a stacktrace in the error log.
def test_exception_basic():
    print("starting test")
   # raise AssertionError("sample assertion error")  # this is equivalent to assert False, "sample assertion error"
    print("after raise")

    # what print statements do you see when you run the above code - in the "captured output"? what is the stack trace?
    # After studying both. Comment out the raise and proceed further.
    print("part 2 begin")
    try:
        print("part 2 entered try")
        assert True, "sample error"
    except ArithmeticError as er:
        print("part 2, caught an arithmentic error")
        print (er)
        raise
    except AssertionError as ae:
        print("part 2, caught an assertion error")
        print (ae)
        raise
    finally:
        print("part 2, in finally block")

    # again study what prints you got and the print of exception and make sure you understand the control flow of an
    # an exception.
    # make the assert to True to pass the test and then proceed to the next set of tests.
'''when assert is false
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 11, in test_exception_basic
AssertionError: sample error
starting test
after raise
part 2 begin
part 2 entered try
part 2, caught an assertion error
sample error
part 2, in finally block
'''
''' when assert is true
starting test
after raise
part 2 begin
part 2 entered try
part 2, in finally block'''


test_notes = """
In the following tests, to track the control flow, we use a 'result' list to mark the control flow points visited 
during execution. The contents of the 'result' at the end depend on which code paths were executed and which were not.
 
you must reason about the control flow and fill in the assert statement with the expected value of 'result'.
"""


def test_exception_flow_1():
    fruit = "orange"
    result = []
    try:
        fruit = fruit.upper()
        result.append("one")
        fruit.missingmethod() # what happens to the control flow here?
        result.append("two")  # will this line get executed?
    except AttributeError as ae:
        result.append("three")

    assert ['one', 'three'] == result

def test_exception_flow_2():
  fruit = "orange"
  result = []
  try:
    try:
        result.append("one")
        value = 1/0             #division by zero.
        result.append("two")
        fruit.missingmethod()   #missing attribute
        result.append("three")
    except ZeroDivisionError as ze:
        result.append("five")
  except AttributeError as ae:
        result.append("four")
  assert ['one', 'five']== result

def test_raise_error():
    result = []
    try:
        result.append("one")
        raise AttributeError("some error here")
    except AttributeError as se:
        result.append("three")

    assert ['one', 'three'] == result

def test_missing_except():
    result = []
    fruit = "orange"
    try:
      result.append("one")
      #what happens now? fix it with an appropriate try except so that result is as expected.
      fruit.missingmethod()
    except AttributeError as ae:
      result.append("two")

    assert ["one", "two"] == result

# this function manages its exception itself, raises no exception
def function_handle_exception(result):
    fruit = "orange"
    result.append("f:enter")
    try:
        fruit.missingmethod()
    except AttributeError as ae:
        result.append("f:except")

    result.append("f:return")

# this function raises an exception to the caller.
def function_raise_exception(result):
    fruit = "orange"
    result.append("f:enter")
   # fruit.missingmethod()
   # result.append("f:return")
    try:
        fruit.missingmethod()
    except AttributeError as ae:
        result.append("f:except")

    result.append("f:return")


# call a function that does not raise exception to caller
def test_function_call_noexception():
    result = []
    try:
        result.append("m:beforecall")
        function_handle_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall'] == result

# test a function call that raises exception to caller
def test_function_call_withexception():
    result = []
    try:
        result.append("m:beforecall")
        function_raise_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall'] == result

# behavior of else clause when an exception is raised in try
def test_else_on_exception():
    result = []
    try:
        result.append("m:beforecall")
        function_raise_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    else:
        result.append("m:else")

    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall', 'm:else'] == result

# behavior of else clause when no exception is raised in try
def test_else_on_no_exception():
    result = []
    try:
        result.append("m:beforecall")
        function_handle_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    else:
        result.append("m:else")

    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall', 'm:else'] == result

# behavior of finally when an exception in raised in try
def test_finally_on_exception():
    result = []
    try:
        result.append("m:beforecall")
        function_raise_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    else:
        result.append("m:else")
    finally:
        result.append("m:finally")

    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall', 'm:else', 'm:finally'] == result


# behavior of finally when no exception is raised in try
def test_finally_on_no_exception():
    result = []
    try:
        result.append("m:beforecall")
        function_handle_exception(result)
        result.append("m:aftercall")
    except AttributeError as ae:
        result.append("m:except")
    else:
        result.append("m:else")
    finally:
        result.append("m:finally")

    assert ['m:beforecall', 'f:enter', 'f:except', 'f:return', 'm:aftercall', 'm:else', 'm:finally'] == result


import traceback
# Sometimes in the process of handling one exception another one may be raised.
# Python 3 has implicitly tracks the inner exception and also allows you to replace one exception with another.
def test_nested_exceptions():
   try:
    try:
        raise AssertionError('inner error ')
    except AssertionError as ae:
        raise AssertionError("error in except")
    finally:
        raise AssertionError("error in finally")
   except AssertionError as ae:
        print(ae)

    # run the above and see the exception trace

    # enclose the entire code above in another try catch and just print the exception in the
    # new catch instead of allowing the AssertionError to be raised from the test method.
    # This will pass the test. Also note what you get from the print

    # note: did you really see the exception traceback in the pytest output when tests passes? :-)
    # Try to figure it out on your own for an hour and discuss on forums if you could
    # not get this to work.


notes2 = '''
Go through this to have a general idea of all the exceptions raised by python
https://docs.python.org/3/library/exceptions.html
'''

three_things_i_learnt = """
-
-
-
"""
