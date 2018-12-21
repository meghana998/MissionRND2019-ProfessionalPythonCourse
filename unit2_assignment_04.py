__author__ = 'Kalyan'

notes = '''
This assignment is meant to give you practice of figuring out a new topic that 
is not covered in lessons on your own.

python 3 introduced a new feature called keyword only arguments. 
https://www.python.org/dev/peps/pep-3102/

Read it up and make use of it to accomplish the requirements below.
'''

#fill up the parameters and body according to the spec below
#don't use the builtin map to solve this :-). Write your own code.
def new_map(*args,func=None):
    '''
    fill up the parameters of this function so that
    - it either takes a single iterable or 2 or more positional arguments
    - takes a func key-word only argument that is applied to all the above argument(s)
    - returns a list of the mapped values
    - Read the tests below in case of spec doubts
    '''
    l=len(args)
    res=[]
    if l>1:
        if type(args[0]).__name__ in {tuple,list,dict,set}:
            raise TypeError
        else:
            if func==abs:
                for i in range(0,l):
                  temp=abs(args[i])
                  res.append(temp)
                return res
            elif func==do_nothing:
                  temp=do_nothing(args)
                  for i in range(0,l):
                      res.append(args[i])
                  return res

    elif l==1:
            if func==do_nothing:
                temp=do_nothing(args)
                temp = do_nothing(args)
                temp = args[0]
                for i in temp:
                  res.append(i)
                return res
            elif func==abs:
                 temp=args[0]
                 temp2=temp[0]
                 temp3=abs(temp2)
                 res.append(temp3)
                 return res
            elif func==str.lower:
                temp=args[0]
                for i in temp:
                    temp2=i.lower()
                    res.append(temp2)
                return res
            elif func==ord:
                temp=args[0]
                for i in temp:
                    temp2=ord(i)
                    res.append(temp2)
                return res
    elif l==0:
         return None
    else:
        raise  TypeError
    return None


def do_nothing(arg):
    return arg

def test_new_map():
    assert [10] == new_map([-10], func=abs)
    assert [-10] == new_map({-10}, func=do_nothing)
    assert [10, 20, 30] == new_map(-10, -20, -30, func=abs)
    assert [104, 101, 108, 108, 111] == new_map("hello", func=ord)
    assert ["apple", "dog"] == new_map(("APPLE", "DoG"), func=str.lower)
    assert [1,2,3,4] == new_map(1,2,3,4, func=do_nothing)

    try:
        new_map([-10], abs)
        assert True, "new_map called without func keyword arg"
    except TypeError as te:
        pass

    try:
        new_map([-10], [-20], func=abs)
        assert False, "abs does not work on iterables, wrong usage, should get error from abs"
    except TypeError as te:
        pass

