#!/usr/bin/env python
# Written by: DGC

import abc

#==============================================================================
class ImmutableContainer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __len__(self):
        raise
    
    @abc.abstractmethod
    def __getitem__(self, key):
        raise
    
#==============================================================================
class MutableContainer(ImmutableContainer):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __setitem__(self, key, value):
        raise

    @abc.abstractmethod
    def __delitem__(self, key):
        raise

#==============================================================================
class Iterable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __iter__(self):
        raise

#==============================================================================
class ReverseIterator(Iterable):
    """ 
    Iterates the object given to it in reverse so it shows the difference. 
    """

    def __init__(self, iterable_object):
        self.list = iterable_object
        # start at the end of the iterable_object
        self.index = len(iterable_object)

    def __iter__(self):
        # return an iterator
        return self

    def next(self):
        " Return the list backwards so it's noticably different."
        if (self.index == 0):
            # the list is over, raise a stop index exception
            raise StopIteration
        self.index = self.index - 1
        return self.list[self.index]

if (__name__ == "__main__"):
    days = [
        "Monday",
        "Tuesday", 
        "Wednesday", 
        "Thursday",
        "Friday", 
        "Saturday", 
        "Sunday"
        ]
    it = ReverseIterator(days)
    for day in it:
        print(day)
