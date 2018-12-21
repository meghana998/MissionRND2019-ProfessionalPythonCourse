__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
import collections
def are_anagrams(first, second):
   '''
   if (first==None )or (second==None):
       return False
   elif (first==" " )or (second==" "):
        return False
   elif (first == "") or (second == ""):
       return False
   else:
       if " " in first:
          second=second+" "
       if " " in second:
           first=first+" "
       if " " not in second or " " not in first:
         if len(first)!=len(second):
           return False
       first = first.lower()
       second = second.lower()
       f=list(first)
       h=second
       for i in h:
           if(i in f):
               continue
           else:
               return False
   return True
   '''
   import collections

   if first == None or second == None:
       return False

   f = first.lower()

   s = second.lower()

   a = collections.Counter(f)

   b = collections.Counter(s)

   if list(a - b) == []:

       return True

   else:

       return False

# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams(None, "tip")
    assert False == are_anagrams("pit", None)
    assert False == are_anagrams("pit", "hip")
    assert True == are_anagrams("pit", "pit")
    assert True == are_anagrams("rail safety" ,"fairy tales")
    assert True == are_anagrams("roast beef" , "eat for BSE" )
    assert True == are_anagrams("customers" ,"store scum")
    assert True == are_anagrams("William Shakespeare" ,"I am a weakish speller")
    assert False == are_anagrams("1233", "123")
    assert False == are_anagrams(None, None)
    assert False == are_anagrams("bigg","big")
    assert False == are_anagrams("bigg", "biig")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
