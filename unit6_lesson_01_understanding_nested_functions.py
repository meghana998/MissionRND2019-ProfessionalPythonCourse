__author__ = 'Kalyan'

notes = '''
nested functions underlie many advanced features of python. So a basic understanding of this
feature is essential to mastering python.

nested functions are defined in the scope of a function, behave exactly the same except
that they have a read only access to variables in the outer function.
'''

from placeholders import *

def outer_func(outer_var):
    def inner_func(inner_var):
        return outer_var + inner_var
    return inner_func
'''************************************************************************************************ '''
def test_inner_func_scope():
    # inner_func not accessible by default
    try:
        inner_func()
    except NameError:  # fill up the exception
        pass

    # this syntax does not work either, it is not just static scoping.
    try:
        outer_func.inner_func()
    except AttributeError : # fillup the exception
        pass

def test_inner_func_can_be_returned():
    f1 = outer_func(10)
    assert 'function' == type(f1).__name__
    assert 30 == f1(20)

def test_each_invocation_returns_a_new_func():
    f1 = outer_func(10)
    f2 = outer_func(10)

    assert False == (f1 is f2)
    assert False == (f1 == f2)

    f3 = f2
    assert True == (f3 is f2)
    assert True == (f3 == f2)

def test_inner_func_has_access_to_outer_variables_after_return():
    f1 = outer_func(20)
    f2 = outer_func(50)

    assert 50 == f1(30)
    assert  60 == f1(40)

    assert 80 == f2(30)
    assert 90 == f2(40)

def print_attributes(obj):
    for x in dir(obj):
        print("attribute: " + x)
        print(getattr(obj, x))

def test_inner_func_attributes():
    f1 = outer_func(10)
    assert 35 == len(dir(f1)) #how many attributes does f1 have

    # use the print_attributes function to explore the properties
    # fill up the attribute name that you think holds a reference to the
    # function scope variables
    ref_to_outer_scope = 'global'
# if you understand this, you have understood nested funcs :).
# Also a good idea to use the visualizer to understand this code...
def test_inner_func_late_binding():
    def outer():
        funcs = []
        for x in range(5):
            def inner():
                return x
            funcs.append(inner)
        result = []
        for func in funcs:
            result.append(func())
        return result

    assert [4, 4, 4, 4, 4] == outer()

# just to re-iterate what you have learnt above. Search if this is not clear!
def test_inner_func_late_binding2():
    def outer(nums):
        def inner():
            nums.append(10)

        assert [10,20,30] == nums # see the function invocation below.
        inner()
        assert [10,20,30,10] == nums
        # assign nums to another empty list
        nums = []
        inner()
        assert [10] == nums
        inner()
        assert [10,10] == nums

        return inner

    # I have called all variables nums, so you can check if you understanding of names
    # and scopes is right :-).
    nums = [10, 20, 30]
    f1 = outer(nums)
    assert [10, 20, 30, 10] == nums
    f1()
    assert [10, 20, 30, 10]== nums

# generally you should not write code like this :), this is only to learn
def test_outer_scope_reads():
    y = 30
    def outer(x):
        def inner1():
            x = 30
            return x
        def inner2():
            return x + y
        def inner3():
            # note what happens to outer y here
            y = 10
            return x + y

        return [inner1(), inner2(), inner3(), x, y]

    assert[30, 50, 30, 20, 30]== outer(20)
def test_outer_scope_write():
    y = 10
    def outer(x):
        def inner1():
            nonlocal y  # this syntax allows you to bind to outer y
            y = 40
            return y

        def inner2():
            y = 30
            return y

        def inner3():
            return y
        return [x, y, inner1(), inner2(), inner3()]

    assert [25, 10, 40, 30, 40] == outer(25)

# def is an executable statement. the function name is nothing more than a name
# binding to a code object! So same scope rules as variables apply to function names.
# read up more at http://effbot.org/zone/default-values.htm
def test_def_is_a_statement():
    def outer(x):
        if x > 10:
            def f():
                return x * 2
        else:
            def f():
                return x * 3
        return f

    assert 40 == outer(20)()
    assert 15 == outer(5)()


three_things_i_learnt = """
-scope of the functions inside the functions
-nested functions 
-how to return and assign the func name and what happens when it gets deleted(orginal one)
"""
