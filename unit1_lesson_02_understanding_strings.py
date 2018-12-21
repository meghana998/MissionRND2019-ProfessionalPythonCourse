__author__ = 'Kalyan'

from placeholders import *

notes = """
 string is one of the most commonly used data types, it used to represent textual data.
 It has different behavior than a char* in C. 

 I recommend you to do this lesson by experimenting in the console.  Run each test individually in 
 py.test and fix each one, one assert at a time.
 
 Start reading online documentation/resources only if you are not able to figure it out by experiment.
"""

def test_string_type():
    assert 'str'== type("Hello World").__name__
    assert True== isinstance("Hello World", str)

def test_single_quoted_strings_are_strings():
    assert True== isinstance('Hello World', str)

def test_double_quoted_strings_are_strings():
    assert True == isinstance("Hello World", str)

def test_triple_quoted_strings_are_strings():
    assert True == isinstance("""Hello World""", str)

def test_triple_single_quoted_strings_are_strings():
    assert True== isinstance('''Hello World''', str)

def test_raw_strings_are_strings():
    # raw string literals are specified using the r before the first quote
    # raw strings are used to avoid escaping backslashes, usually useful
    # when specifying things like window's paths which use backslash. e.g. r"c:\work\myfile.ini"

    assert True == isinstance(r"Hello \n World", str)
    assert 1 == len("\n")
    assert 2 == len(r"\n")

    # write a non-raw string in the ___ to make both strings equal.
    assert "Hello\\n" == r"Hello\n"

def test_single_quoted_strings_can_embed_double_quotes():
    first = 'The pilot said "Jump"'
    #ability to embed the other quote avoids the hassle of escaping quotes in strings
    second = "The pilot said \"Jump\""  #note back slash escaping of "
    are_equal = (first == second)
    assert True == are_equal

def test_double_quoted_strings_can_embed_single_quotes():
    first = "The pilot said 'Jump'"
    second = 'The pilot said \'Jump\''  #note back slash escaping of '
    are_equal = (first == second)
    assert True == are_equal

def test_triple_quoted_strings_can_have_both_single_and_double_quotes():
    """ Edit tq_str to make are_equal True """
    tq_str = """ Isn't the "Hobbit" great? """
    dq_str = """ Isn't the \"Hobbit\" great? """
    are_equal = (tq_str == dq_str)
    assert True== are_equal

def test_triple_quoted_strings_can_span_lines1() :
    tq_str = """HelloWorld"""
    dq_str =  "HelloWorld" # what is the double quoted form of tq_str
    assert (tq_str == dq_str)

def test_string_len():
    assert 13 == len("Hello 'world'")
    assert 13 == len('Hello \'world\'')

def test_triple_quoted_strings_can_span_lines2():
    string="HelloWorld"
    assert True == isinstance(string, str)
    assert 10 == len(string)

def test_strings_can_be_indexed():
    string = "Hello"
    assert 'H' == string[0]
    assert 'e'== string[1]
    assert 'l' == string[2]
    assert 'l' == string[3]
    assert 'o' == string[4]
    assert 'o' == string[-1]  # solves the common use case to iterate from end
    assert 'l' == string[-2]
    assert 'l' == string[-3]
    assert 'e' == string[-4]
    assert 'H' == string[-5]
    assert 'H' == string[-0]  # hint -0 is 0
    assert 5 == len(string)
    try:
        out_of_bounds = string[5] #raises an error, we will revisit exceptions later
    except IndexError as ie:
        print(ie)
        assert True  #make this True to proceed.

def test_chars_are_strings_too():
    string = "Hello"
    first_char = string[0]
    assert 'str'== type(first_char).__name__
    assert 'str' == type('a').__name__
    assert  'str'== type("a").__name__

def test_strings_are_immutable():
    """ strings in python cannot be modified unlike in C """
    string = "Hello"
    try:
        string[0] = "M"
    except TypeError as te:
        # run this test alone in py.test and observe the  'FAILURES' section and 'Captured stdout call' section
        # at the end. see the error messages in FAILURES and the print statements in "Captured stdout call"
        # Print statements can be added to failing tests and can be  observed in a similar manner
        print("Can you see me in pytest output?")
        print(te)
        assert True   # after you observe, make this True to proceed.

def test_string_concat():
    assert 'Hello  world' == "Hello " + " world"
    assert  'Hello world'== """Hello """ + 'world'
    assert 'Hello world' == 'Hello ' + "world"


def test_string_slicing():
    """ Slicing creates new strings """
    string = "Hello world"
    #with begin : end
    assert '' == string[0:0]

    assert 'He' == string[0:2]
    assert  'ello' == string[1:5]
    assert  'ello worl'== string[1:-1]
    assert 'llo wor' == string[2:-2]

    #with :end, note usage of negative indices as well.
    assert '' == string[:0]
    assert 'Hell' == string[:4]
    assert  'Hello worl'== string[:-1]

    #with begin:
    assert 'Hello world' == string[0:]
    assert 'o world' == string[4:]
    assert 'd' == string[-1:]

    #observe the invariant
    assert 'Hello world' == string[:0] + string[0:]
    assert 'Hello world'== string[:1] + string[1:]
    assert 'Hello world' == string[:2] + string[2:]
    assert 'Hello world' == string[:3] + string[3:]


def test_string_repeat():
    assert 'HelloHelloHello' == "Hello" * 3
    assert 12 == len("Hello " * 2)
def test_string_combine():
    """
    Use slicing to pass the assert.
    """
    hello = "Hello World"
    bye = "Goodbye moon"
    assert bye[0:7] + hello[5:]== "Goodbye World"

def test_string_formatting():
    greeting = "Hello '{0}'".format("learner")
    assert "Hello 'learner'" == greeting

    truth = "{1} plus {1} makes {0}".format('two','one')
    assert truth == "one plus one makes two"

    stmt = "{name} is {age} years old".format(name="Ravi", age=25)
    assert "Ravi is 25 years old"== stmt

def test_string_formatting_literals():
    """
    literals which start with f are implicitly treated as expressions which are evaluated at runtime.
    This makes formatting a little more easier to understand.
    The full details are at: https://www.python.org/dev/peps/pep-0498/, read it to get an idea of how a feature
    is introduced into python.
    """
    value = 10
    assert 'value is: 10'== f"value is: {value}"
    value = 20
    assert 'value is: 30' == f"value is: {value + 10}"
    name, age = "Ramu", 20
    assert  "Ramu is 20 years old!" == f"{name} is {age} years old!"

def test_string_membership():
    assert False == ('c' in 'apple')  #is there a precedence issue here or something else?
    assert True == ('a' in 'apple')
    assert True == ('app' in 'apple')

def test_string_methods():
    word = "hello"
    assert "Hello" == word.capitalize()
    assert '  hello   ' == word.center(10)
    assert '00000hello' == word.zfill(10)
    assert 'hezebrazebrao' == word.replace("l", "zebra")
    # you can experiment with all methods on string in console
    # by entering "something". (enter the dot too) to pop up all the available methods.



#Now apply what you have learnt above.
def rotate_right(input, count):
    """
    write a single line of code using what you have learnt in this lesson - slicing and concat
    assume 0 <= count <= len(input)
    """

    return input[(-count):]+input[0:(count*-1)] # replace __ with the code

def test_rotate():
    assert 'hello' == rotate_right("hello", 0)
    assert 'ohell' == rotate_right("hello", 1)
    assert 'lohel' == rotate_right("hello", 2)
    assert 'llohe' == rotate_right("hello", 3)
    assert 'elloh' == rotate_right("hello", 4)
    assert 'hello' == rotate_right("hello", 5)

notes2 = '''
Read this after you finish the lesson:
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
'''

three_things_i_learnt = """
-rotateright
-concatenatio and slicing
-string functions
"""
