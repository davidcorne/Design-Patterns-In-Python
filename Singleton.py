#!/usr/bin/env python
# Written by: DGC

class Singleton(object):
    """ A generic base class to derive any singleton class from. """
    __instance = None

    def __new__(new_singleton, *arguments, **keyword_arguments):
        """Override the __new__ method so that it is a singleton."""
        if not new_singleton.__instance:
            print("An actual new instance of Singleton made.")
            print("")
            new_singleton.__instance = object.__new__(new_singleton)
            new_singleton.__instance.init(*arguments, **keyword_arguments)
        return new_singleton.__instance

class GlobalState(Singleton):

    def init(self):
        self.value = 0
        print("init() called once")
        print("")

    def __init__(self):
        print("__init__() always called")
        print("")

if (__name__ == "__main__"):
    a = GlobalState()
    # value is default, 0
    print("Expecting 0, value = %i" %(a.value))
    print("")

    # set the value to 5
    a.value = 5

    # make a new object, the value will still be 5
    b = GlobalState()
    print("Expecting 5, value = %i" %(b.value))
    print("")
    print("Is a == b? " + str(a == b))
