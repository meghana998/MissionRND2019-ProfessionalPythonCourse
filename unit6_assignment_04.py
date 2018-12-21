__author__ = 'Kalyan'

problem_notes = '''
For this assignment create a decorator which can be used for count profiling.
ans:

Python includes a profiler called cProfile. It not only gives the total running time,
 but also times each function separately, and tells you how many times each function was called,
  making it easy to determine where you should make optimizations.
You can call it from within your code, or from the interpreter, like this:

import cProfile
cProfile.run('foo()')

Even more usefully, you can invoke the cProfile when running a script:
python -m cProfile myscript.py
To make it even easier, I made a little batch file called 'profile.bat':
python -m cProfile %1
So all I have to do is run:
profile euler048.py
And I get this:
1007 function calls in 0.061 CPU seconds



@count_calls:
- add a count attribute to the function
- count keeps track of number of calls made to the function. If the function is recursive, give a parameter
to track only top level call and not the sub calls.

You may want to give special behavior for how this decorators behave when exceptions are raised etc. but for now
just count all calls irrespective of error status.

Assume that this decorators are used in single threaded programs only for now.

I used count for testing simplicity, you could write @time_calls decorator in a very similar spirit. Try it out as a
personal exercise and see what all design issues you hit when you chain it with above!
'''
from functools import lru_cache

def count_calls(skip_recursion=True):
      def inner(func):
        if skip_recursion:
         @lru_cache()
         def tmp(*args, **kwargs):
            tmp.count += 1
            return func(*args, **kwargs)
         tmp.count=0
         return tmp
        else:
            def tmp(*args, **kwargs):
                tmp.count += 1
                return func(*args, **kwargs)

            tmp.count = 0
            return tmp
      return inner

def test_calls_decorator():
    @count_calls()
    def fib(n):
        if n <= 0:
            raise ValueError("n <= 0")
        if n == 1 or n == 2:
            return 1

        return fib(n-1) + fib(n-2)

    assert [1, 1, 2, 3, 5 ] == [fib(i) for i in range(1,6)]
    assert 5 == fib.count # only top calls counted.


    # with recursion, count all calls, but time only top level calls.
    @count_calls(skip_recursion=False)
    def fib(n):
        if n == 1 or n == 2:
            return 1

        return fib(n-1) + fib(n-2)

    assert [1, 1, 2, 3, 5 ] == [fib(i) for i in range(1,6)]
    assert 19 == fib.count # all calls counted.

