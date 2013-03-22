#!/usr/bin/env python
# Written by: DGC

# python imports

#==============================================================================
class MonoState(object):
    __data = 5
    
    def __init__(self):
        pass

    @property
    def data(self):
        return MonoState.__data

    @data.setter
    def data(self, value):
        MonoState.__data = value

#==============================================================================
if (__name__ == "__main__"):
    m_1 = MonoState()
    print("First data:  " + str(m_1.data))
    m_1.data = 4
    m_2 = MonoState()
    print("Second data: " + str(m_2.data))
    print("First instance:  " + str(m_1))
    print("Second instance: " + str(m_1))
    print("These are not singletons, so these are different instances")
    
