__author__ = 'Kalyan'

from placeholders import *

notes = """
This lesson explores some advanced features of functions. This will help you make sense
of a lot of standard library functions when you use them. In particular, the following are covered

- positional and keyword arguments
- defining and passing variable number of positional and keyword arguments 
- unpacking arguments

Be sure to understand the difference between a parameter and an argument. Keep these links open and refer to them
as you do the lesson!

https://docs.python.org/3/glossary.html#term-parameter
https://docs.python.org/3/glossary.html#term-argument
https://docs.python.org/3/reference/expressions.html#calls
"""

def demo(first, second, third=3, fourth=4):
    '''
    This is a test function that has some default and non-default parameters. Use the test below to study how the
    arguments are bound at runtime and the various ways in which the function can be invoked.
    '''
    return [first, second, third, fourth]


# parameters with defaults allows you to write one api without having a large number
# of overloads for various scenarios.
# define the above function in console and play with each of the invocations and see the error messages carefully.
# NOTE: add extra arguments where necessary. First note what error you get and then fix the function invocations.
def test_function_call_with_keyword_arguments():
    assert [10,10,3,4] == demo(10,10)
    assert [10, 20, 3, 4] == demo(10, 20)
    assert [10, 20, 30, 4] == demo(10, 20, 30)
    assert [10, 20, 3, 4] == demo(10,second=20)
    assert [10, 20, 30, 4] == demo(first=10,second=20, third=30)
    assert [10, 20, 30, 4] == demo(first=10,second=20, third=30)
    assert [10, 20, 30, 4] == demo(first=10,second=20,third=30)
    assert [10, 20, 10, 4]==demo(first=10,second=20,third=10)  # is this allowed? correct and uncomment 10 or first=10




# The *args syntax is used to specify that you can pass variable number of arguments to a function.
# args is a var-positional parameter -> variable number of positional arguments can be bound to it at runtime.
def demo_variable_args(first, *args):
    return args  #just return args so we can inspect its nature in the test.

# assumes args are all strings
def my_merge(separator, *args):
    return separator.join(args)


def test_function_with_variable_args():
    result = demo_variable_args("hello", "world")
    assert 'tuple' == type(result).__name__ #this is the type of args
    assert ('world',) == result              #this is the value of args

    assert (1, 2, 3) == demo_variable_args("hello", 1, 2, 3)

    assert 'one.two.three' == my_merge(".", "one", "two", "three")
    assert'one,two,three' == my_merge(",", "one", "two", "three")


# **kwargs can be used to pass additional named arguments in addition to the specified parameters
# kwargs is a var-keyword parameter that can be bound to a variable number of named keyword arguments that don't map to any other
# function parameter at runtime.
def demo_with_keyword_args(name, *args, **kwargs):
    return kwargs  # return kwargs to inspect it.


def test_function_with_keyword_args():
    result = demo_with_keyword_args("jack", age=10, height=100)
    assert 'dict' == type(result).__name__
    assert {'age': 10, 'height': 100} == result
    assert {'age': 10, 'height': 100} == demo_with_keyword_args("jack", "address", age=10, height=100)
    assert {'address': 'address', 'age': 10, 'height': 100} == demo_with_keyword_args("jack", address="address", age=10, height=100)
    assert {} == demo_with_keyword_args(name="jack") # what do you observe here?


# this is function which accepts a variable number of positional arguments
# and variable number of keyword arguments. Note what comes into args and kwargs based on how you call.
def demo_var_kw(*args, **kwargs):
    return args, kwargs

def demo_unpacking(name, *args, **kwargs):
    return demo_var_kw(*args, **kwargs)


def demo_no_unpacking(name, *args, **kwargs):
    return demo_var_kw(args, kwargs)


# Unpacking sequences into arguments is useful when you are calling other
# functions which take variable/kw args. Also read
# Walk through the visualizer, first read the code a couple of times and then step through in full screen mode :)
# https://goo.gl/KqTnJv

def test_function_unpacking():
    result = demo_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert ((1, 2), {'k1': 'v1', 'k2': 'v2'}) == result

    result = demo_no_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert (((1, 2), {'k1': 'v1', 'k2': 'v2'},),{}) == result

    result = demo_var_kw(1,2, k1="v1")
    assert ((1, 2), {'k1': 'v1'}) == result

    result = demo_var_kw((1,2), {"k1" :"v1"})
    assert (((1, 2), {'k1': 'v1'}), {}) == result

    result = demo_var_kw(*(1,2), **{"k1": "v1"})
    assert ((1, 2), {'k1': 'v1'}) == result

    #you can unpack lists as well
    result = demo_var_kw(*[1,2], **{"k1":"v1"})
    assert ((1, 2), {'k1': 'v1'}) == result        ####unpackingg  **,*



# Apply what you learnt:
# This function shows how variable arguments can be useful to define certain kinds of functions
def simple_format(format, *args):
    s=' '.join(args)
    s=s.split(' ')
    count=0
    for j in s:
        count=count+1
    for i in range(0,count):
        temp=s[i]
        temp2=''
        format=format.replace('%'+str(i),temp)
    return  format



def test_simple_format():
    assert "hello hari" == simple_format("hello %0", "hari")
    assert "hari calls ashok and %2" == simple_format("%1 calls %0 and %2", "ashok", "hari")
    assert "hari says hari"  == simple_format("%0 says %0", "hari")
    assert "hari calls ashok"  == simple_format("%1 calls %0", "ashok", "hari")

note2 = '''
Go through this link: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
All of that should make sense now and there should be no surprises.
'''

three_things_i_learnt = """
- positional and keyword arguments
- defining and passing variable number of positional and keyword arguments 
- unpacking arguments
"""

"""
    Returns a formatted string by replacing all instances of %X with Xth argument in args (0...len(args))
    e.g. "%0 says hello", "ted" should return "ted says hello"
    "%1 says hello to %0", ("ted", "jack") should return jack says hello to ted etc.
    If %X is used and X > len(args) it is returned as is.
    """