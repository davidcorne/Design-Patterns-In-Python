#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Adapter(object):
    
    def __init__(self):
        print("initalised")

def test(value, message):
    """ This asserts against the value printing for either pass or fail. """
    assert value, message
    print("PASSED: %s" %(message))
    print("")

#==============================================================================
if (__name__ == "__main__"):
    test(True, "This is a passing test")
    test(False, "This is a failing test")
