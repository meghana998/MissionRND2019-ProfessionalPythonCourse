__author__ = 'Kalyan'

from placeholders import *

notes = '''
python list is a ordered mutable sequence of objects. You will see that some
of the ideas/concepts that are introduced in strings also apply to lists 
(slicing, indexing etc).

experiment in console to learn and make these tests pass.
'''

def test_list_type():
    fruits = ["banana", "orange", "grape"]
    assert 'list' == type(fruits).__name__

def test_list_len():
    fruits = ["banana", "orange", "grape"]
    assert 3== len(fruits)

def test_list_can_be_indexed():
    fruits = ["banana", "orange", "grape"]
    assert "banana" == fruits[0]
    assert "orange" == fruits[1]
    assert "grape" == fruits[2]
    assert "grape" == fruits[-1]
    assert "orange" == fruits[-2]
    assert "banana"== fruits[-3]

def test_list_is_mutable():
    fruits = ["banana", "orange", "grape"]
    fruits[0] = "mango"
    assert ["mango", "orange", "grape"] == fruits  #replace __ with expected contents of list

def test_list_can_be_sliced():
    """
     Slicing works the same as on strings
    """
    fruits = ['banana', 'orange', "grape"]
    assert [] == fruits[0:0]

    #begin : end
    assert ['banana', 'orange'] == fruits[0:2]
    assert ['banana', 'orange', 'grape'] == fruits[0:5]
    assert ['orange'] == fruits[1:-1]

    # begin :
    assert ['banana', 'orange', "grape"] == fruits[0:]
    assert ["grape"] == fruits[2:]
    assert  ['banana', 'orange', "grape"]== fruits[0:]

    #: end
    assert [] == fruits[:0]
    assert ['banana', 'orange'] == fruits[:2]
    assert ['banana', 'orange', "grape"] == fruits[:5]

    # note the invariant
    assert ['banana', 'orange', "grape"] == fruits[:1] + fruits[1:]


def test_slice_creates_a_new_list():
    fruits = ["banana", "orange", "grape"]
    slice = fruits[0:2]
    slice.append("guava")

    assert ["banana", "orange", "grape"] == fruits # did this change?
    assert ["banana", "orange", "guava"] == slice


def test_list_merge():
    fruits = ["banana", "orange", "grape"]
    veggies = ["beetroot", "tomato"]
    all = fruits + veggies

    assert ['banana', 'orange', 'grape', 'beetroot', 'tomato']== all
    assert ['banana', 'orange', 'grape']== fruits
    assert ['beetroot', 'tomato']== veggies
    assert  ['orange', 'grape', 'beetroot'] == fruits[1:] + veggies[:1]

def test_list_slice_replacement_is_inplace():
    fruits = ["banana", "orange", "grape"]

    fruits[1:2] = ["litchi", "guava"]
    assert ['banana', 'litchi', 'guava', 'grape'] ==fruits

    fruits[3:] = []
    assert ['banana', 'litchi', 'guava']== fruits

    fruits[:2] = []
    assert ['guava'] == fruits

def test_list_common_methods():
    """
     You can find methods supported by lists by entering []. (note the dot)
     in the python console. the autocomplete will pop up all the available methods
     on the list.

     For help on a specific function like pop enter help([].pop) in console
    """
    fruits = []
    fruits.append("orange")

    assert ["orange"]== fruits

    fruits.insert(0, "banana")
    assert ['banana', 'orange'] == fruits

    fruits.append(["litchi","guava"])
    assert ['banana', 'orange', ['litchi', 'guava']] == fruits

    fruits.reverse()
    assert [['litchi', 'guava'], 'orange', 'banana'] == fruits

    fruits.pop()
    assert [['litchi', 'guava'], 'orange'] == fruits

    fruits.pop(0)
    assert ['orange']== fruits

def test_list_can_contain_lists():
    fruits = ["orange", "banana"]
    veggies = ["beetroot", "tomato"]
    all = [fruits, veggies]

    assert 2 == len(all)
    assert ['orange', 'banana'] == all[0]
    assert ['beetroot', 'tomato'] == all[1]

def test_list_can_contain_objects_of_different_types():
    # note that this is rarely done in practice!
    mixed = ["string", 10]
    assert 'string' == mixed[0]
    assert 10== mixed[1]

def test_list_sort():
    numbers = [ 5, 4, 3, 8 ]
    numbers.sort()
    assert [3, 4, 5, 8] == numbers
    numbers.sort(reverse=True)
    assert [8, 5, 4, 3] == numbers

# if something unexpected happens see,
# https://docs.python.org/3/reference/expressions.html#comparisons
# and fix accordingly.
def test_list_membership():
    numbers = [ 5, 4, 3]
    assert True ==( 5 in numbers)
    assert False ==( 10 in numbers)


# you will understand how this works in later lessons (the next 2 tests).
# for now understand the behavior.
def test_list_range():
    # range objects can be used to generate lists of numbers of all kinds
    # note that you need to pass a range object to list constructor to create the
    # the list.
    # print (range.__doc__)
    numbers = list(range(1,5))
    assert [1, 2, 3, 4] == numbers

    numbers = list(range(1, 5, 2))
    assert [1,3] == numbers


def test_list_from_string():
    # you can create lists from other sequences like objects like strings.
    result = list("hello")
    assert ['h', 'e', 'l', 'l', 'o'] == result


#Now apply what you have learnt. Type  help(range) in console or read online docs
def odd_desc(count):
    """
    Replace ___ with a single call to range to return a list of descending odd numbers ending with 1
    For e.g if count = 2, return a list of 2 odds [3,1]. See the test below if it is not clear
    """
    return list(reversed(range(1,count*2,2)))

def test_odd_desc():
    assert [] == odd_desc(0)
    assert [1] == odd_desc(1)
    assert [7,5,3,1] == odd_desc(4)
    assert [11,9,7,5,3,1] == odd_desc(6)


three_things_i_learnt = """
-slicing
-reversing range differently
-list replacing inplace
"""