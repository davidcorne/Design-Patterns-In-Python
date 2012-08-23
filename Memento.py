#!/usr/bin/env python
# Written by: DGC
# undo

import copy

#==============================================================================
class something(object):
    
    def __init__(self):
        self.a = 0
        self.undo_helper = UndoHelper(self)

    def undo(self):
        #print("revert %i" %(self.undo_helper.revert().a))
        self = self.undo_helper.revert()
        
    def add(self, number):
        self.a += number
        self.undo_helper.append(self)

#==============================================================================
class UndoHelper(object):
    
    def __init__(self, something):
        self.history = [something]

    def revert(self):
        #print("revert"),
        #for i in self.history:
        #    print(i.a),
        #    print("")
        print(self.history)
        return self.history[0]

    def append(self, item):
        self.history.append(copy.deepcopy(item))

#==============================================================================
if (__name__ == "__main__"):
    s = something()
    s.add(5)
    print(s.a)
    s.add(5)
    print(s.a)
    s.add(5)
    print(s.a)
    s.undo()
    print(s.a)
