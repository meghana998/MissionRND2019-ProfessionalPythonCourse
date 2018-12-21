__author__ = 'Kalyan'

notes = '''
Python allows users to add user defined types via classes. This allows you to augment
builtin types like dict, list, tuple with your own types with their own specific behavior.

Like most common languages like java and c#, python supports objected oriented features
like class definitions, inheritance and polymorphism.

However, unlike java and c#, python does not insist that you have to forcibly model your
problem domain as classes if it does not make sense. You could use any mix of modules,
functions and classes to model your application. For e.g. if you goal is to code up the
fibonacci function or write a routine that sorts a sequence, defining a class
does not make sense.
'''

from placeholders import *

notes_1 = '''
 We are defining the classes in the function scope so that we can redefine them for every test.
 Generally you would define them at the module scope.
'''


#classes are objects too, they have a type, have attributes, can be passed
# to functions, held in data structures etc.
def test_classes_are_objects():
    class TestQueue:
        """TestQueue empty class."""
        pass

    def get_attr_count(obj):
        return len(dir(obj))

    assert 'type' == type(TestQueue).__name__ #note this.
    assert 'TestQueue empty class.' == TestQueue.__doc__
    assert 26 == get_attr_count(TestQueue)

def test_classes_are_callable_objects():
    class TestQueue:
        pass

    #classes are callable objects just like function objects
    assert True == callable(TestQueue)


def test_classes_are_object_factories():
    class TestQueue:
        pass

    q1 = TestQueue()  # you can 'call' a class to create an instance
    q2 = TestQueue()

    assert  'TestQueue' == (q1.__class__).__name__
    assert   'TestQueue' == (q2.__class__).__name__

    assert False == (q1 is TestQueue)
    assert  False== (q2 is TestQueue)
    assert False == (q2 is q1)

    assert True== isinstance(q1, TestQueue)
    assert  True == isinstance(q2, TestQueue)

    assert 26 == len(dir(TestQueue))
    assert 26 == len(dir(q1))
    assert  26 == len(dir(q2))


# if an __init__ method exists it is called with the object that is
# being created, so you can initialize it.
def test_classes_init_initializer():
    test_list = []

    class TestQueue:
        def __init__(self):
            assert True, "Entered here !"
            test_list.append(self)

    q1 = TestQueue() # fix the assert to pass this.
    self_argument = test_list[0]
    assert True == (self_argument is q1)

def test_classes_init_with_args():
    class TestQueue:
        def __init__(self, name):
            self.name = name

    # note the lack of first argument, see the previous method for what is self.
    q1 = TestQueue("q1")
    q2 = TestQueue("q2")

    assert 'q1' == q1.name
    assert 'q2' == q2.name

    try:
        q3 = TestQueue()
    except TypeError: #what error do you get?
        pass


#just like def, class is also a runtime statement which bounds a class name with the class body code
def test_class_is_an_executable_statement():
    def create_class(value):
        if (value > 10):
            class TestQueue:
                def __init__(self):
                    self.name = ">10TestQueue"
        else:
            class TestQueue:
                def __init__(self):
                    self.name = "<=10TestQueue"

        return TestQueue

    Q_class = create_class(20)
    q1 = Q_class()
    assert '>10TestQueue' == q1.name

    Q_class = create_class(5)
    q1 = Q_class()
    assert '<=10TestQueue' == q1.name


# the self argument name is just a convention but it is
# followed widely, so don't change the name of the first argument
# this is in contrast to other languages where the instance is implicit via
# the 'this' keyword.
def test_classes_methods():
    class TestQueue:
        def __init__(self, name):
            self.name = name
            self._TestQueue = []

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    q1 = TestQueue("q1")
    q1.push(10) #note that we pass only one argument
    assert 10 == q1.pop()

    #above is a equivalent to
    TestQueue.push(q1, 10)
    assert 10 == TestQueue.pop(q1)


def test_classes_bound_and_unbound_methods():
    class TestQueue:
        def __init__(self, name):
            self.name = name
            self._TestQueue = []

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    q1 = TestQueue("q1")
    q1_push = q1.push

    assert False == (q1.push is TestQueue.push)

    assert AttributeError,"Unbounded method" == TestQueue.push.__self__   #unbound method
    assert AttributeError,"Bounded method" == q1_push.__self__      #bound method, is associated with an instance

    # now understand the output of these 2 statements.
    print (q1.push)
    print (TestQueue.push)
    # make this true once you have seen the output of the prints. py.test suppresses the output of passing tests!
    assert True

def test_classes_can_have_state():
    class TestQueue:
        count = 0
        def __init__(self, name):
            self.name = name
            self._TestQueue = []
            TestQueue.count += 1

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    assert 0 == TestQueue.count
    q1 = TestQueue("q1")
    assert 1 == TestQueue.count
    q2 = TestQueue("q2")
    assert 2 == TestQueue.count

    # if instance has not state, it is looked up in the class.
    # generally a bad practice to access ClassState through an instance.
    assert 2 == q1.count


def test_instances_state():
    class Record:
        pass

    r1 = Record()
    # note that we added an attribute called name into r1 at runtime
    r1.name = "jack"

    r2 = Record()
    # note that we added an attribute called age into r2 at runtime
    r2.age = 20

    try:
        name = r2.name
        assert False, "Should not reach here"
    except AttributeError: # fill up the exception you got
        assert True

    try:
        age = r1.age
        assert False, "Should not reach here"
    except AttributeError : #what exception do you get?
        assert True

    r2.name = "harry"
    r1.age = 15

    assert 'harry' == r2.name
    assert 15 == r1.age

    #Note that though python allows you to add instance specific
    #state, you should rarely use it as it can lead to very buggy
    #code as you deal with instances with different attributes.

    #it is always a good idea to define an init method and assign default values that cannot be given a value
    class Record2:
        # if for some reason you cannot fill up all attributes at construction time, give defaults like below.
        def __init__(self):
            self.name = None
            self.age = -1

notes_2 = '''
 Now that you have used classes for sometime,
 read through: http://docs.python.org/3/tutorial/classes.html
 Ignore the parts about inheritance for now.
'''

# Now create your first class based on what you have learnt.

# write a class Person with attributes name, age, weight (kgs), height (ft) and takes
# them through the constructor and exposes a method get_bmi_result()
# which returns one of "underweight", "healthy", "obese"
# http://en.wikipedia.org/wiki/Body_mass_index
class Person:
    def __init__(self,name,age,heigth,weight):
        self.name=name
        self.age=age
        self.weight=weight
        self.heigth=heigth
        self.heigth=self.heigth
        self.res=["healthy","underweight","obese"]

    def get_bmi_result(self):
        i=0
        w=0
        h=0
        w=int(self.weight)
        h=int(self.heigth)
        h=h*0.3048
        i=w/((h)**2)
        if 18.5<=i and i<= 25:
           return self.res[0]
        elif i<=18.5:
            return self.res[1]
        elif i>=30:
            return self.res[2]





def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()

three_things_i_learnt = """
-
-
-
"""