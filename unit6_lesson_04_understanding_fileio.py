__author__ = 'Kalyan'

notes = '''
Python has a good api to deal with text and binary files. We explore that
in this module. You may notice how much this is easier than the corresponding c api :-).

Use help(file.XXX) to find help on file method XXX (tell, seek etc.)

'''

from placeholders import *

import inspect
import os

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir

# open files generated as a part of the tests. Allow them to be in a different dir via DATA_DIR
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

#opens a file from the module directory for reading. These are input files that are part of course material
#and must be submitted along with this lesson.
#Read: https://docs.python.org/3/library/functions.html#open
def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def test_file_readlines():
    f = open_input_file("unit6_input_data.txt")
    lines = f.readlines()
    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] == lines


def test_file_read():
    f = open_input_file("unit6_input_data.txt")
    data = f.read()
    assert 'one\ntwo\nthree\nfour\nfive\n' == data


def test_file_end():
    f = open_input_file("unit6_input_data.txt")
    s = f.read() # read till end.
    assert '' == f.read()
    assert ''== f.read()


def test_file_read_binary():
    f = open_input_file("unit6_input_data.txt", "rb")
    lines = f.readlines()
    assert [b'one\r\n', b'two\r\n', b'three\r\n', b'four\r\n', b'five\r\n']== lines
    f.seek(0, 0)
    data = f.read()
    assert  b'one\r\ntwo\r\nthree\r\nfour\r\nfive\r\n' == data


def test_file_windows_newlines():
    f = open_temp_file("newlines_tmp.txt", "wb")
    # what does encode do? why do you need it?, run this code without it and explore.
    f.write("one\r\ntwo\rthree\n".encode())
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rt")
    assert 'one\ntwo\nthree\n' == f.read()
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rb")
    data = f.read()
    assert  b''== f.read()


    #windows behavior : https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files


def test_file_universal_newlines():
    f = open_temp_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n".encode())
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rU")
    assert 'one\ntwo\nthree\n'== f.read()
    assert ('\r','\n','\r\n') == f.newlines


def test_file_readline():
    f = open_input_file("unit6_input_data.txt")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)

    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] == lines


#files can be used as iterable objects!
def test_file_iteration():
    f = open_input_file("unit6_input_data.txt")
    lines = []
    # this will not read the whole file into memory like readlines would.
    for x in f:
        lines.append(x)
    assert ['one\n', 'two\n', 'three\n', 'four\n', 'five\n']== lines


def test_file_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt")
    while True:
        line = f.readline()
        tells.append(f.tell())
        if not line:
            break
    assert [5, 10, 17, 23, 29, 29] == tells


def test_file_readlines_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt", "rb")
    for line in f.readlines():
        tells.append(f.tell())

    assert [29, 29, 29, 29, 29]== tells


def test_file_iteration_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt", "rb")
    for line in f:
        tells.append(f.tell())

    assert [5, 10, 17, 23, 29] == tells # is there really no difference between readlines and iteration?
    # as an exercise do both this text and previous test in rt mode. discuss your
    # observations and findings on forums.


def test_file_seek():
    f = open_input_file("unit6_input_data.txt", "rb")
    assert 0 == f.tell()
    f.read()
    assert  29 == f.tell()
    assert b'' == f.read()

    f.seek(0, 0)
    assert b'one\r\ntwo\r\nthree\r\nfour\r\nfive\r\n' == f.read()
    f.seek(-3, 2)
    assert b'e\r\n' == f.read()
    f.seek(-2, 1)
    assert  b'\r\n' == f.read()

#windows has a few newlines quirks.
def test_file_write_text():
    f = open_temp_file("test_write.txt", "w") # same as "wt"
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_temp_file("test_write.txt", "rb")
    assert b'one\r\ntwo\r\nthree\r\n'== f.read()

    f = open_temp_file("test_write.txt", "rt")
    assert 'one\ntwo\nthree\n' == f.read()


def test_file_write_binary():
    f = open_temp_file("test_write.txt", "wb")
    f.write("one\ntwo\nthree\n".encode())
    f.close()

    f = open_temp_file("test_write.txt", "rb")
    assert b'one\ntwo\nthree\n' == f.read()

    f = open_temp_file("test_write.txt", "rt")
    assert 'one\ntwo\nthree\n' == f.read()


# It is generally a good practice to close files after their use is over
def test_file_close():
    f = open_input_file("unit6_input_data.txt")
    assert  False == f.closed
    try:
        lines = [line.strip() for line in f.readlines()]
    finally:
    # putting it in finally so that it is closed even if an exception is raised
        f.close()
    assert True == f.closed

# http://effbot.org/zone/python-with-statement.htm
# you can close files with a 'with' statement irrespective of exceptions.
# This is similar to using statement in c#
def test_with_statement():
    try:
        with open_input_file("unit6_input_data.txt") as f:
            assert  True == f.closed
            raise Exception("some random exception")
    except Exception as ex:
        print(ex)
        pass

    assert True == f.closed

def test_file_iteration1():
    with open_input_file("unit6_input_data.txt") as f:
        lines = []
        # we are walking through f as an iterator, so even if file is huge this code acts like a buffered reader!!
        for line in f:
            lines.append(line.strip())
        assert  ['one', 'two', 'three', 'four', 'five'] == lines

        lines = []
        for line in f:
            lines.append(line.strip())
        # what happened here? read the link i gave above.
        assert [] == lines

# a common pattern to load files into an in memory list
# after doing something on each line (for e.g. strip and upper in this case)
# notice how little code gets so much work done!
def test_file_iteration2():
    def process(input):
        return input.strip().upper()

    with open_input_file("unit6_input_data.txt") as f:
        data = [process(line) for line in f]
        assert ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'] == data


three_things_i_learnt = """
-stripping and uppera nd lower for input of file
-input and output of file
-accessing ie iterative and readlines and os some more properites
"""