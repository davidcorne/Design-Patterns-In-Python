#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class UnitTest(object):
    
    def __init__(self):
        for test in dir(self):
            # ignore the magic methods
            if (test[0:2] != "__" and test != "setup"):
                print("Running test: \"" + str(test) + "\"")
                # get the function object from the internal dictionary and call
                # it
                self.__getattribute__(test)()

#==============================================================================
def test(value, message):
    """ This asserts against the value printing for either pass or fail. """
    assert value, message
    print("PASSED: %s" %(message))
    print("")

