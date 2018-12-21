__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
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

def get_temp_file(file):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    return os.path.join(data_dir, file)

'''def get_input_file(file):
    mod_dir = get_module_dir()
    return  os.path.join(mod_dir, file)
'''

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
'''******************************************'''
def get_input_file(source):
   f = open_input_file(source)
   data = f.readlines()
   return data


def filter_the_data(data):
    data.remove('\n')
    for i in data:
        l = list(i)
        if "#" in l:
            data.remove(i)
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    return data

def group_anagrams(data):
    l = map(lambda x: x.lower(), data)
    groups = [list(group) for key, group in groupby(sorted(l, key=sorted), sorted)]
    return groups

def sort_anagrams(groups,data):
    for i in groups:
           i.sort(key=lambda x: x.lower())
    groups.sort(key=lambda x:x[0].lower())
    groups.sort(key=lambda s:len(s),reverse=True)
    #map the words to original words
    for i in range(len(groups)):
       for j in range(len(groups[i])):
            for k in data:
                if groups[i][j] == k.lower():
                    groups[i][j] = k
    return groups

def put_output_file(groups):
    f1 = open_temp_file("unit7_output_01.txt", "w")
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            f1.write(groups[i][j])
            f1.write("\n")
    f1.close()

def anagram_sort(source):
    data = get_input_file(source)
    filtered_data = filter_the_data(data)
    groups = group_anagrams(filtered_data)
    sorted_anagrams = sort_anagrams(groups,filtered_data)
    put_output_file(groups)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        source = argv[1]

        anagram_sort(source)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())