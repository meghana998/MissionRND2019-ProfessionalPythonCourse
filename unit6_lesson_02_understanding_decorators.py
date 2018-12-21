__author__ = 'Kalyan'

notes = '''
 Decorators are higher order functions that add behavior to other functions. Python provides a simple syntax that makes
 it easy to use decorators on existing functions. This makes it easy to define higher order behaviors that can applied
 to other functions without repeating the same behavior in every function.

 To get an idea of how python folks introduces language features and spec them out read the PEP:
 http://legacy.python.org/dev/peps/pep-0318/

 Review all the previous function lessons including nested functions if required and remember that
 functions are first class objects in python!
'''

from placeholders import *

# This is a function that adds enter log to another function by wrapping
# the func call with additional log behavior.

def log(func):
    # the inner function has access to outer func locals and they are bound at definition
    # time via a closure.
    def inner():
        print(("Entering func", func.__name__))
        return func()
    return inner  # returns a new func.

# This is how you would do it, without any help from python.
def test_decorators_old_way():
    # A dummy method for testing.
    def get_hello():
        return "hello"

    assert 'get_hello' == get_hello.__name__
    assert 'hello' == get_hello()

    # Check that there is no log statement from the above invocation to get_hello in the pytest output and then
    # remove the assert. Logs are not shown for passing tests to reduce output verbosity.
  # assert False
    # now we are creating a new version of get_hello by invoking log.
    # now get_hello is bound to a new function returned by log!
    get_hello = log(get_hello)

    #while the variable name is get_hello, the actual function is something else now!
    assert 'inner' == get_hello.__name__
    # the result is same
    assert 'hello' == get_hello()

    # check the pytest output now and remove the assert after that. Search for  "Captured stdout call"...
    #assert False

    # we can use the same log method to decorate any number of functions
    # Thus promoting reusable behavior that can be applied to any function

    # Another dummy method for testing.
    def get_bye():
        return "bye"

    assert  'get_bye' == get_bye.__name__
    assert 'bye' == get_bye()

    # Note that we could have held the return value in a new name.
    # By binding it to the original function name, we augment the functionality for the users
    # of get_hello or get_bye.
    dummy = log(get_bye)

    #nothing changes so far.
    assert 'get_bye'== get_bye.__name__
    assert 'bye' == get_bye()

    #if we rebind get_bye then stuff changes and we get logging behavior
    get_bye = dummy # same as get_bye = log(get_bye)
    assert 'inner'== get_bye.__name__
    assert'bye' == get_bye()

    # remove after verifying that get_bye is now logging.
    # assert False


def test_decorators_syntax():
    # Note this new syntax which does exactly what we did in previous test.
    # (ie) invocation of log with get_hello and reassigning the result func to get_hello
    @log
    def get_hello():
        return "hello"

    assert 'inner'== get_hello.__name__
    assert  'hello' == get_hello()

    # check pytest output and then remove the assert.
    #assert False;

def test_decorators_promote_reuse():

    def get_hello():
        return "hello"

    def get_bye():
        return "hello"

    def get_sorry():
        return "sorry"

    # decorate all those 3 methods with log behavior. Note that we have augmented functionality of all functions
    # with the same decorator.
    assert 'get_hello' == get_hello.__name__
    assert  'get_bye' == get_bye.__name__
    assert  'get_sorry' == get_sorry.__name__

    #while they have same name, they are not the same method (why?)
    get_hello()
    get_bye()
    get_sorry()

    # check log output to see different log statements from each and then remove assert!
   # assert False


def test_decorators_func_arguments():
    # to make testing easy we are going to append logs to this list instead of printing them!
    test_logs = []
    # how can we write decorators for functions which take arguments?
    # what do we do when we don't know arguments before hand?
    def log(func):
        def inner(a,*args):
            # keeping log_stmt simple for testing, we can print argument values etc.
            # to make it useful for real.
            log_stmt = "Entered: " + func.__name__
            test_logs.append(log_stmt)
            return func(a,*args)

        return inner

    # Note that we want to apply the same decorator to many functions
    @log
    def add(a, b):
        return a + b

    @log
    def sub(a, b):
        return a - b

    @log
    def increment(a):
        return a+1

    test_logs = []
    assert 30 == add(10, 20)
    assert ['Entered: add'] == test_logs

    test_logs = []
    assert 5 == sub(30, 25)
    assert ['Entered: sub'] == test_logs

    test_logs = []
    assert 13 == increment(12)
    assert ['Entered: increment'] == test_logs


def test_decorator_chaining():
    def pass_through1(func):
        def inner1(a,*args):
            test_logs.append("pt1")
            return func(a,*args)
        return inner1

    def pass_through2(func):
        def inner2(a,*args):
            test_logs.append("pt2")
            return func(a,*args)
        return inner2

    @pass_through1
    @pass_through2
    def add(a,b):
        return a + b

    test_logs = []
    assert 30 == add(10,20)
    assert 'inner1'== add.__name__
    assert ['pt1', 'pt2'] == test_logs

    # reverse order of decorators, what happens?
    @pass_through2
    @pass_through1
    def increment(a):
        return a+1

    test_logs = []
    assert 11 == increment(10)
    assert 'inner2'== increment.__name__
    assert ['pt2', 'pt1'] == test_logs

def test_decorators_arguments():
    # Some times we want to parameterize the decorators. In that case
    # you write a decorator generator that is then applied on the function!

    # Write a decorator generator which can be used to decorate test methods so that
    # they run only if a particular environment variable is defined, else they are skipped.
    # This sort of functionality is common in any testing framework to run certain tests on certain platforms only

    import os
    test_logs=[]
    # Define this decorator generator to work for arbitrary environment variables, see the usage to see how it is used

    def runif(variable):
        def inner(func):
            def wrapper():
                if variable in os.environ:
                    return func()
                else:
                    return None
            return wrapper
        return inner

    # run this only if MY_LINUX env variable is present
    @runif("MY_LINUX")
    def linux_test():
        test_logs.append("linux_test called!")

    # run this only if MY_WINDOWS env variable is present
    @runif("MY_WINDOWS")
    def windows_test():
        test_logs.append("windows_test called!")

    # if you have defined runif correctly, these tests should pass.



    test_logs = []
    # first no variables are defined.
    linux_test()
    windows_test()
    assert [] == test_logs

    os.environ["MY_LINUX"] = "1"
    test_logs = []
    linux_test()
    windows_test()
    assert ["linux_test called!"] == test_logs

    os.environ["MY_WINDOWS"] = "1"
    test_logs =[]
    linux_test()
    windows_test()
    assert ["linux_test called!", "windows_test called!"] == test_logs



def test_decorators_wraps():
    # NOTE: some of these decorators have common bugs, fix them as you go along :-)

    def pass_through1(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner

    @pass_through1
    def add(a, b):
        "adds 2 numbers"
        return a + b

    # Note that we have lost useful information like documentation and name, which are used by
    # code inspection tools and help generators.
    assert 'inner' == add.__name__
    assert None== add.__doc__
    assert None== add(10,20) # execution works fine

    # preserving these is a common usecase. We can modify our decorators to preserves these.
    # modify this decorator to preserve func_name and func_doc by copying them over to the wrapper function.
    def pass_through2(func):
        def inner(*args):
            func(*args)
        return func

    @pass_through2
    def sub(a, b):
        "subtracts 2 numbers"
        return a - b

    # these should have actual values now!
    assert 'sub'== sub.__name__
    assert 'subtracts 2 numbers'== sub.__doc__
    assert 10 == sub(20, 10)

    # since this behavior is commonly required. python gives an out of box feature to preserve these and
    # other function attributes. See https://docs.python.org/2/library/functools.html#functools.wraps
    import functools
    def pass_through3(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return func

    @pass_through3
    def mult(a,b):
        return a*b

    assert 'mult' == mult.__name__
    assert None == mult.__doc__
    assert 200 == mult(10,20)

# As a final exercise try to create your own version of wraps decorator generator that preserves just these
# 2 attributes and see if you understood the whole thing :)!
def test_decorators_custom_wrap():
    # This is your own implementation of wraps.
    def wraps(func):
        def inner(*args):
            return func
        return inner

    # fix any bugs in the decorator just like before
    def pass_through(func):
        @wraps(func)
        def inner(*args):
            func(*args)
        return func

    @pass_through
    def add(a, b):
        'adds 2 numbers'
        return a + b

    assert 'add' == add.__name__
    assert 'adds 2 numbers' == add.__doc__
    assert 30 == add(10, 20)


three_things_i_learnt = """
-old decoraators
-decorators
-parameterized decos and wraps also
"""