__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

import string
digs = string.digits + string.ascii_letters

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    sign=0
    try:
        if base<2:
            raise ValueError
        if base>36:
            raise ValueError
        if  type(number).__name__!='int':
            raise TypeError
        if  type(base).__name__!='int':
            raise TypeError
        if number==None:
            raise TypeError
        if number < 0:
            sign = -1
        elif number == 0:
            return digs[0]
        else:
            sign = 1
        number *= sign
        digits = []
        while number:
            digits.append(digs[int(number % base)].capitalize())
            number = int(number / base)
        if sign < 0:
            digits.append('-')
        digits.reverse()
        return ''.join(digits)
    except:
         return None

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert True, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert True, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert True, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert True, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert True, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
