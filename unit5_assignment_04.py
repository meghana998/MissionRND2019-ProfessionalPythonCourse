__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''


def left_binary_search(input, value):
    if input == []:
        return -1
    if value==None:
        return -1
    l = len(input)
    if input[0] == value:
        return 0
    low = 0
    high = len(input)
    while low <= high:
        if low == high:
            if value not in input:
                return -1
            else:
                return low
        mid = int(low + (high - low) / 2)
        if input[mid] == value:
            if mid == 0:
                return 0
            if input[mid - 1] == value:
                high = mid
            elif input[mid - 1] != input[mid]:
                return mid
        elif input[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 0==left_binary_search([1,1,1,1,1,1,1,1], 1)
    assert 2==left_binary_search([2,3,4,4,4,4], 4)
    assert 1 == left_binary_search([2, 4, 4, 4, 4, 4], 4)
    assert 5 == left_binary_search([2, 3, 3, 3, 3, 4], 4)
    assert 5 == left_binary_search([3, 3, 3, 3, 3, 4], 4)
    assert 5 == left_binary_search([2, 3, 3, 3, 3, 4], 4)
    assert 0 == left_binary_search([-1, -1, -1, 3, 3, 4], -1)
    assert -1 == left_binary_search([], None)
def test_left_binary_search():
    input=range(10)
    for index,value in enumerate(input):
        assert index== left_binary_search(input,value)
    assert -1== left_binary_search(input,-10)
    assert -1==left_binary_search(input,100)
    assert -1 ==left_binary_search([],10)
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
