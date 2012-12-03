#!/usr/bin/env python
# Written by: DGC

import sys
# renamed module in python 3
if (sys.version_info[:2] < (3,0)):
    from Tkinter import *
else:
    from tkinter import *

#==============================================================================
class Email(object):
    
    def __init__(self):
        print("initalised")

#==============================================================================
class EmailViewModel(object):
    
    def __init__(self):
        print("initalised")

#==============================================================================
class View(object):
    
    def __init__(self):
        self.viewmodel = EmailViewModel()
        self.parent = Tk()
        self.make_window()
        self.parent.withdraw()
        
    def make_window(self):
        self.window = Toplevel(self.parent)
        self.window.title("MVVM Email")
        # hook up the delete button so that it quits the window and doesn't 
        # make the main program hang
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)

    def show(self):
        self.parent.mainloop()

#==============================================================================
if (__name__ == "__main__"):
    window = View()
    window.show()
