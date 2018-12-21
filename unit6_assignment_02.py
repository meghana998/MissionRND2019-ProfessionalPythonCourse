__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
4. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
5. Review the files lesson and write elegant code. Python api/features makes it possible to write concise and efficient code.
'''

import inspect
import os
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

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
def get_temp_file(file):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    return os.path.join(data_dir, file)

# returns file path from module directory. These are input files that are part of course material
def get_input_file(file):
    mod_dir = get_module_dir()
    return  os.path.join(mod_dir, file)
def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

import unit6utils

def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    f = open_input_file(source)
    data = f.readlines()
    data.remove('\n')
    for i in data:
        l = list(i)
        if "#" in l:
            data.remove(i)
    for i in range(len(data)):
        data[i] = data[i].lower()
    data.sort()
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    f = open_temp_file(destination, "w")
    for i in data:
       f.write(i)
       f.write("\n")
    f.close()
    
def test_sort_words():
    source = unit6utils.get_input_file("unit6_testinput_02.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
    destination = unit6utils.get_temp_file("unit6_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
