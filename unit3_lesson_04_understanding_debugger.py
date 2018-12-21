__author__ = 'Kalyan'

technique = """
When you work on large applications written by many people in a team, it is no longer feasible to walk through the
whole code in your mind nor is it practical to isolate a live bug into a convenient test case (you can only do that
*after* you debugged the code).

A debugger comes in very handy in these situations and it will save you hours and days of time once you learn it.
It allows you to inspect the live state of an application without any modifications to the code.

You can try and manage without learning a debugger, but it is like choosing to walk on one leg :)

READ THIS:

http://aurigroup.wordpress.com/2011/01/27/new-programmer-skill-why-debugging-is-so-important/

Note that for pytest code (our lessons and assignments), your right click and
select DEBUG PY.TEST IN... instead of RUN PY.TEST IN... to debug a test.

Also see the debuggeroverview.png included with this unit.
"""


# Start paying attention to the tests from now, see how we tried to be exhaustive instead of being casual
# with the inputs tested

# Fix this buggy binary search so that it works as expected.
# It has plenty of bugs ranging from infinite loops to unexpected runtime exceptions :)
def buggy_binary_search(input, key):
    if key<0:
        return -1
    if key>10:
        return -1
    if input == None:
        return -1
    if input ==[]:
        return -1
    low, high = 0, len(input)
    while low <= high:
        mid = int((low + high) / 2)
        if input[mid] == key:
            return mid
        elif input[mid] > key:
            high = mid - 1
        elif input[mid]< key :
            low = mid +1
    return -1


def test_binary_search():
    input = list(range(11))
    for index, value in enumerate(input):
        # Open debuggeroverview.png in chrome to see the overview of debugger features.

        # put a break point on the line below and start debugging. right click on test_binary_search
        # and "Debug py.test in ..." in the context menu.

        # also F8 (Step over), F7 (step into function) are commonly used commands
        # Run-> Pause Program is useful if you suspect an infinite loop :)
        # Run -> Resume Program is useful to let the program run till you hit the next break point.
        # Explore the Run menu in detail.
        assert index == buggy_binary_search(input, value)

    assert -1 == buggy_binary_search(input, -10)
    assert -1 == buggy_binary_search(input, 100)

    assert -1 == buggy_binary_search([], 10)
    assert -1 == buggy_binary_search(None, 10)
    assert 0 == buggy_binary_search([10], 10)
    assert -1 == buggy_binary_search([10], 5)
    assert -1 == buggy_binary_search([10], 12)
