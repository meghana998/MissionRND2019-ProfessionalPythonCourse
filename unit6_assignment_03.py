__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''
import unit6utils
from itertools import groupby
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


def anagram_sort(source, destination):
    f = open_input_file(source)
    data = f.readlines()
    data.remove('\n')
    for i in data:
        l = list(i)
        if "#" in l:
            data.remove(i)
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    l = map(lambda x: x.lower(), data)
    groups = [list(group) for key, group in groupby(sorted(l, key=sorted), sorted)]
    for i in groups:
        i.sort(key=lambda x: x.lower())
    groups.sort(key=lambda x:x[0].lower())
    groups.sort(key=lambda s:len(s),reverse=True)
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            for k in data:
                if groups[i][j] == k.lower():
                    groups[i][j] = k
    f1 = open_temp_file(destination, "w")
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            f1.write(groups[i][j])
            f1.write("\n")
    f1.close()
    f.close()


def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
