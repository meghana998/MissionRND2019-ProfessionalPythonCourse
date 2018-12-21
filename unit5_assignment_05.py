__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    s = []
    temp = ''
    index1=0
    index2=0
    if sentence== None:
        return None
    if len(sentence)==0:
        return None
    for c in sentence:
        if c == ' ':
            s.append(temp)
            temp = ''
        else:
            temp += c
    if temp:
        s.append(temp)
    for i in range(0,len(s)):
        if s[i]=="either":
            index1=i
            break
    for i in range(0,len(s)):
        if s[i]=="or":
            index2=i
            break
    if (index1==0) or (index2==0):
            return sentence
    if index1==index2-1:
        return sentence
    if index1>index2:
        return sentence
    res1=[]
    res2=[]
    for i in range(0,index1):
        res1.append(s[i])
    for i in range(index1+1,index2):
        res2.append(s[i])
    res1=" ".join(res1)
    res2=" ".join(res2)
    res1=res1+" "+res2
    return res1


def test_prune_either_or_student():
    assert "we could go to a movie"== prune_either_or("we could either go to a movie or a hotel")
    assert "we could go either to a movie" == prune_either_or("we could either go either to a movie or a hotel")
    assert "if it is not of the correct form," == prune_either_or("if it is not of the correct form,")
    assert " " == prune_either_or(" ")
    assert "@#$%^^&" == prune_either_or("@#$%^^&")
    assert "k" == prune_either_or("k")
    assert "[]" == prune_either_or("[]")
    assert "123445" == prune_either_or("123445")
    assert "some random either or test" == prune_either_or("some random either or test")
    assert None == prune_either_or(None)
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
