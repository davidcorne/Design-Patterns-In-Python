#!/usr/bin/env python
# Written by: DGC

class Singleton(object):
    instance = None
    number = 0
    array = []
    string = ""

    def __init__(self):
        self.reset_var = 0
        print("Some initialisation.")
        print("")

    def __new__(new_singleton):
        """Override the __new__ method so that it is a singleton."""
        if not new_singleton.instance:
            new_singleton.instance = super(Singleton, new_singleton).__new__(new_singleton)
            print("An actual new instance of Singleton made.")
            print("")
        return new_singleton.instance
    
    def output(self):
        print("My number is:"),
        print(self.number)
        print("My array is:"),
        print(self.array)
        print("My string is:"),
        print(self.string)
        print("My variable that's reset on creation is:"),
        print(self.reset_var)
        print("")

if (__name__ == "__main__"):
    instance_one = Singleton()
    instance_one.reset_var = 5
    instance_one.output()

    # now change instance_one, make a new Singleton() and see if it's worked
    instance_one.number = "I'm not a number!!"
    instance_one.array = 14
    instance_one.string = [1, 1, 2]

    instance_two = Singleton()
    instance_two.output()
    
