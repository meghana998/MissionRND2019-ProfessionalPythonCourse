__author__ = 'Kalyan'

from placeholders import *

notes = '''
This lesson introduces the basic assert statement in python. assert is generally used to 'assert' the truth of an
expression. It takes the form assert <expr>, <optional message>. If <expr> evaluates to False an AssertionError is raised with
the <optional message>. If is evaluates to True, nothing happens and execution moves to the next statement in the function.

In the tests below, replace the blanks with values so that the resulting expression is True.

Recommended flow to do the lessons is given below. This approach comes in handy as we move to 
more complex topics even if this is seem trivial at this point.

- attempt each test_XXX method individually instead of doing all of them at one go. The test names are chosen to tell you
  what you need to understand to solve the test :-)
- you can run a single method by placing cursor on method name and right click -> 'run py.test in...' this run just 
  the single test
- study the failure error messages in py.test window
- fix the code with your expected code and re-run the test till the code passes. 
- Use the python console (Alt+P) to experiment, refer to online python docs, google search etc. if something is not clear.
- go to the next method once you have resolved a method.

Note: ___ is just a constant to make the code valid python code, you need to replace it with correct values. DO NOT 
CHANGE the placeholders.py file which defines the constant!
'''


def test_assert_true():
    assert True #This should be True -- replace ___ with True.

def test_assert_true_with_message():
    print("test print")
    assert True, "This is the failure message" # what error do you see when you run this test?
                                              # replace ___ with True to stop seeing the assertion error

def test_assert_equality():
    assert 7== 2 + 5   #replace __ with the expected value

#Fill in __ in the statements below to make the asserts succeed
def test_make_assert_true_1():
    assert 10 > 7, "Fill in a value greater than 7"

#you can use the interpreter to find the value of 2**30
def test_make_assert_true_2():
    assert 1.07374182e10> 2**30, "Fill in value greater than 2**30"

def test_make_assert_true_3():
    s1 = "Hello, World"
    s2 = "Hello, World"
    assert s1 == s2

three_things_i_learnt = """
-how to run test cases
-how see errors and understood assert and placeholders why and python console 
-what is assert and def
"""