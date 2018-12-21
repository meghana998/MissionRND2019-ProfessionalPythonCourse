__author__ = 'Kalyan'

from placeholders import *

notes = '''
Functions are the basic unit of modularization in python. You use functions to group
together a meaningful action and use it when you need it.

The feature set of functions in python is richer than every major programming
language and makes it easy to expose elegant and usable apis.

This is a big topic, in this lesson we will cover the following:
- functions are first class objects in python! they can be created, assigned, and passed around as any other object 
  as part of regular program flow.
- function documentation
- function return values, parameters and defaults
- defining new functions

be sure to understand 
https://docs.python.org/3/glossary.html#term-parameter
https://docs.python.org/3/glossary.html#term-argument

'''

# here's a simple function. returns nothing
def my_print(x):
    "my_print documentation"
    print(x)

# this is another function. Note the syntax. Returns a value
def my_increment(x):
    return x + 1

# another function, it is common to return multiple values as a tuple.
def my_min_max(numbers):
    return (min(numbers), max(numbers))

# functions are kinds of objects, they have a type too!
def test_function_type():
    assert 'function' == type(my_print).__name__
    assert'function'== type(my_increment).__name__
    assert 'function' == type(test_function_type).__name__

# functions are objects which can be 'called'
def test_function_callable_type():
    assert False == callable(1)
    assert True== callable(my_increment)
    assert False== callable(my_increment(10))

# functions can be held by references just like any other object
def test_function_assignment():
    demo = my_increment
    result = demo(20)
    assert 21== result

# every function returns an object, even when it does not!
def test_every_function_returns_something():
    result = my_print(10)
    assert None == result

    result = my_increment(10)
    assert 11 == result

    result = my_min_max([20, 30, 5])
    assert (5, 30)== result


def demo1():
    """returns 10"""
    return 10


def demo2():
    return 20

#The documentation of every function, if the author wrote it, is available at runtime.
#This makes it easy to access help from console or build specialized help commands like help.
def test_function_documentation():
    assert 'returns 10' == demo1.__doc__
    assert  None== demo2.__doc__


def my_callfunc(func):
    return func()

# functions can be passed around.
def test_functions_can_be_passed_as_objects():
    assert 10 == my_callfunc(demo1)
    assert 20 == my_callfunc(demo2)


# an example of a default parameter
def my_greet(greeting, name="world"):
    return "{0} {1}".format(greeting, name)


def test_default_parameters():
    assert 'Hello world'== my_greet("Hello")
    assert 'Hello john'== my_greet("Hello", "john")


def my_add_to_list1(sequence, target=[]):
    """
    Uses a mutable default, usually leads to unexpected behavior
    """
    target.extend(sequence)
    return target


def my_add_to_list2(sequence, target=None):
    """
    Uses None as default and creates a target list on demand.
    """
    if target is None:
        target = []
    target.extend(sequence)
    return target


def test_function_defaults_are_evaluated_at_definition_time():
    assert ['h', 'i'] == my_add_to_list1("hi")
    assert ['h', 'i', 'b', 'y', 'e'] == my_add_to_list1("bye")

    assert ['h', 'i'] == my_add_to_list2("hi")
    assert ['b', 'y', 'e'] == my_add_to_list2("bye")


reading_note = """
Walk through the visualizer to get a good idea of how functions are defined
and how arguments are passed. 

Experiment with this code in visualizer (see output and the variable references, do it in full screen mode).
https://goo.gl/cwL54H

Do this before proceeding further.
"""

def demo_parameter_passing1(x):
    x = x + 1

def demo_parameter_passing2(names):
    names = []


def demo_parameter_passing3(names):
    names.append("something")


def test_function_params_passed_by_object_reference():
    x = 10
    demo_parameter_passing1(x)
    assert 10 == x

    names = ["one", "two"]
    demo_parameter_passing2(names)
    assert ['one', 'two'] == names

    demo_parameter_passing3(names)
    assert ['one', 'two', 'something'] == names


notes_2 = """
Read this finally :): http://effbot.org/zone/call-by-object.htm

"""

# Most of the python api uses the ability to pass functions as arguments,
# the tests below make you exercise them.

# write your new functions here (use names that do not collide with other names)



# new functions end

def get_word_with_least_vowels(input):
    input=list(input)
    k=[]
    for p in range(len(input)):
        sum=0
        for t in ("a","e","i","o","u"):
            sum=sum+ input[p].count(t)
        k.append(sum)
    for p in range(len(input)):
        sum=0
        for t in ("a","e","i","o","u"):
            sum=sum+ input[p].count(t)
        if sum== min(k):
            break;
    return input[p]



def test_get_word_with_least_vowels():
    assert "fly" == get_word_with_least_vowels(["apple", "joy", "fly"])
    assert "flow" == get_word_with_least_vowels(["apple", "hello", "flow"])
    # same code works for any iterable!
    assert "fly" == get_word_with_least_vowels({"apple", "joy", "fly"})
    assert "flow" == get_word_with_least_vowels(("apple", "hello", "flow"))

def get_min_max_words(input):
   o=[]
   p=[]
   input=list(input)
   i=0
   l=0
   for i in range(len(input)):
       l=len(input[i])
       o.append(l)
   for i in range(len(input)):
       if len(input[i]) == min(o):
           p.append(input[i])
   for i in range(len(input)):
       if len(input[i])==max(o):
           p.append(input[i])
   k=()
   k=tuple(p)
   return k


def test_get_min_max_words():
    assert ("fly", "engine") == get_min_max_words(["fork", "engine", "fly"])
    assert ("fork", "fork") == get_min_max_words(["fork"])
    assert ("fork", "automobile") == get_min_max_words({"fork", "automobile", "tester"})


three_things_i_learnt = """
-
-
-
"""