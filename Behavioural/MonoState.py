#!/usr/bin/env python
# Written by: DGC

# python imports

#==============================================================================
class MonoState(object):
    __data = 5
    
    @property
    def data(self):
        return self.__class__.__data

    @data.setter
    def data(self, value):
        self.__class__.__data = value

#==============================================================================
class MonoState2(object):
    pass

def add_monostate_property(cls, name, initial_value):
    internal_name = "__" + name

    def getter(self):
        return getattr(self.__class__, internal_name)
    def setter(self, value):
        setattr(self.__class__, internal_name, value)
    def deleter(self):
        delattr(self.__class__, internal_name)
    prop = property(getter, setter, deleter, "monostate variable: " + name)
    # set the internal attribute
    setattr(cls, internal_name, initial_value)
    # set the accesser property
    setattr(cls, name, prop)

#==============================================================================
if (__name__ == "__main__"):
    print("Using a class:")
    class_1 = MonoState()
    print("First data:  " + str(class_1.data))
    class_1.data = 4
    class_2 = MonoState()
    print("Second data: " + str(class_2.data))
    print("First instance:  " + str(class_1))
    print("Second instance: " + str(class_2))
    print("These are not singletons, so these are different instances")

    print("")
    print("")
    print("Dynamically adding the property:")
    add_monostate_property(MonoState2, "data", 5)
    dynamic_1 = MonoState()
    print("First data:  " + str(dynamic_1.data))
    dynamic_1.data = 4
    dynamic_2 = MonoState()
    print("Second data: " + str(dynamic_2.data))
    print("First instance:  " + str(dynamic_1))
    print("Second instance: " + str(dynamic_2))
    print("These are not singletons, so these are different instances")

