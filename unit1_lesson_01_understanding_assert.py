__author__ = 'Kalyan'

from placeholders import *

notes = '''
This lesson introduces common numeric types in python. 

For each of these tests use the python console (Alt+P) to fill up the blanks.
type(object) -> returns the object's type.

You can type out a part or entire statement in the console to study it.
For e.g.

>>> type(10)
<class 'int'>
>>> type(10).__name__
'int'

>>> assert __ == type(7).__name__
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name '__' is not defined

>>> assert "hello" == type(7).__name__
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AssertionError

'''

def test_numbers_types():
    assert 'int' == type(7).__name__
    assert 'float' == type(7.5).__name__


import math

def test_numbers_arithmetic_operations():
    assert 30 == 10 + 20
    assert 200 == 10 * 20
    assert 32 == 2 ** 5     # this may be new for you
    assert -10 == 10 - 20
    assert 2== 6/3

    # observe the difference between / and //
    assert 2 == 7 // 3
    assert -3 == -7 // 3
    assert -3== 7 // -3

    # how does the modulo work with negative numbers?
    assert 1 == 7 % 3
    assert 2 == -7 % 3
    assert -2 == 7 % -3

    # floating point numbers are always an issue :-)
    assert 2.3333333333333335 == 7/3

    # comparing floats directly is always a bad idea due to precision errors.
    # Usually you end up testing that they are close enough to some expected value.
    # 'import math' module into console and check help of isclose and fix this assert

    #>>> import math
    #>>> help(math.isclose)
    assert math.isclose(2.33, 7/3, abs_tol=2.33), "fix abs_tol so that this assert passes"


def test_numbers_string_to_int():
    """hint: execute  print(int.__doc__) in python console
       to find out what int(..) does"""
    assert 255 == int("FF", 16)
    assert 63 == int("77", 8)
    assert 3 == int("11", 2)

def test_numbers_int_to_string():
    """hint: these are builtin functions in python and you can experiment with them in console
    """
    assert '0o12' == oct(10)
    assert '0x64' == hex(100)
    assert '0b11111111'== bin(255)

def test_numbers_long():
    """python numbers can be arbitrarily big unlike C"""
    assert 1606938044258990275541962092341162602522202993782792835301376 == 2 ** 200

# Being comfortable with number bases mentally is important and it is routinely asked in interviews as quick test
# of a candidate.
#
# Replace the __ with the correct string representation by working it out on paper (don't use any code or console).
#
# Read the following links:
#           http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
#           https://docs.python.org/3/library/functions.html#int
def test_numbers_base():
    assert 255 == int('0b11111111', 2)
    assert 254 == int('0xfe', 16)
    assert 121 == int('232', 7)
    assert 675 == int('pp', 26)


notes2 = '''
Read this after you finish the lesson for more details on python numeric types: 
https://docs.python.org/3/library/stdtypes.html#typesnumeric
'''

three_things_i_learnt = """
-
-
-
"""