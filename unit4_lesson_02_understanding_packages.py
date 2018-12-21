__author__ = 'Kalyan'

notes = '''
 Sometimes a collection of modules provides related functionality as part of a larger framework,
 then it makes sense to group all of them together. Packages allows you to group related modules together.

 The relationship between packages and modules is similar to that of directories and files in the
 filesystem. Packages can contain sub-packages and modules. 
 
 A module with name a.b.c is saying that c is a module in package b which is a sub-package of package a.
 
'''

from placeholders import *
import sys

# Look at the package1 and package2 directories before starting...

def test_package_basic_import():
    clear_sys_modules()

    print("sys.path value", sys.path)  # note this value in the test output.

    assert False == ("package1" in locals())
    assert False == ("module1" in locals())
    assert  False== ("package1.module1" in locals())

    import package1

    assert True== ("package1" in locals())
    assert False == ("module1" in locals())
    assert False == ("package1.module1" in locals())

    assert 'module' == type(package1).__name__

    assert True == ("package1" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert False== ("package1.module1" in sys.modules)

    try:
        print(package1.module1.__doc__)
    except AttributeError:
        pass

    #modules need explicit import generally.
    import package1.module1
    print(package1.module1.__doc__)

    assert True == ("package1" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert True == ("package1.module1" in sys.modules)


def clear_sys_modules():
    sys.modules.pop("module1", None)
    sys.modules.pop("package1", None)
    sys.modules.pop("package1.module1", None)
    sys.modules.pop("package1.subpackage", None)
    sys.modules.pop("package1.subpackage.m1", None)
    sys.modules.pop("package2", None)
    sys.modules.pop("package2.module2", None)


def test_package_from_import():
    clear_sys_modules()

    assert False == ("package1" in locals())
    assert False == ("module1" in locals())
    assert False == ("package1.module1" in locals())

    from package1 import module1

    assert False == ("package1" in locals())
    assert True == ("module1" in locals())
    assert False == ("package1.module1" in locals())

    assert True== ("package1" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert True == ("package1.module1" in sys.modules)

# https://docs.python.org/3/glossary.html#term-package
def test_package_import_namespacepackage():
    clear_sys_modules()
    # package 2 directory has no __init__.py still it imports as
    # a package in python 3.4+. These are called namespace packages will package1 will be called a regular package.
    import package2
    assert True == ("package2" in sys.modules )
    from package2 import module2
    assert True== ("package2.module2" in sys.modules )


def test_package_sub_packages():
    clear_sys_modules()

    assert False== ("package1" in locals())
    assert False == ("subpackage" in locals())
    assert False == ("package1.subpackage" in locals())

    from package1 import subpackage

    assert False == ("package1" in locals())
    assert True == ("subpackage" in locals())
    assert False == ("package1.subpackage" in locals())

    assert True == ("package1" in sys.modules)
    assert False == ("module1" in sys.modules)
    assert False== ("package1.module1" in sys.modules)
    assert True== ("package1.subpackage" in sys.modules)
    assert False == ("package1.subpackage.m1" in sys.modules)

    #why is this not raising an exception here?
    try:
     print(subpackage.m1.__doc__)
    except:
        pass

    assert False== ("package1.subpackage.m1" in sys.modules)

three_things_i_learnt = """
-
-
-
"""

