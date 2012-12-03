#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Huge(object):
    
    def __init__(self, filename):
        self.read_variables(filename)

    def read_variables(self, filename):
        for i in range(1000000):
            name = "var_" + str(i)
            # would be read from filename
            self.__setattr__(name, i)
            
    def write_variables(self, filename):
        print("Would write to " + filename)

#==============================================================================
class HugeProxy(object):

    def __init__(self, filename):
        self.data = Huge(filename)

#==============================================================================
if (__name__ == "__main__"):
    test_file_vars = Huge("Test File")
    test_file_vars = HugeProxy("Test File")
    test_file_vars = Huge("Test File")
    

