__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

def vowel(ch):
    if ch in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

def converson_into_piglatin(str):
    str=str.split(" ")
    sen=""
    for i in range(len(str)):
        l = list(str[i])
        temp = ""
        if l[-1] == "," or l[-1] == ".":
            temp = l[-1]
            l.remove(temp)
        count = 0
        for j in l:
            if vowel(j):
                break
            else:
                count = count + 1
        from collections import deque
        l = deque(l)
        for i in range(count):
            l.rotate(-1)
        l = list(l)
        lis = ''.join(l)
        lis=lis + temp
        sen=sen+" "+lis
    return sen



def main(argv=None):
   try:
       while True:
           sentence=input()
           print(converson_into_piglatin(sentence))
   except KeyboardInterrupt as ke:
       return 1

if __name__ == "__main__":
    sys.exit(main())