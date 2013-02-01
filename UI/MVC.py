#!/usr/bin/env python
# Written by: DGC

from Tkinter import *

#==============================================================================
class Model(object):
    
    def __init__(self):
        # q_and_a is a dictionary where the key is a question and the entry is
        # a list of pairs, these pairs are an answer and whether it is correct
        self.q_and_a = dict()
        
        self.q_and_a["Is the Earth a sphere?"] = [("Yes", True), ("No", False)]

    def question_and_answer(self):
        """ Returns a randomly chosen question and answer as a pair. """
        key = "Is the Earth a sphere?"
        return (key, self.q_and_a[key])

#==============================================================================
class View(object):

    def __init__(self):
        self.parent = Tk()
        self.controller = None

    def new_question(self, question, answers):
        """ 
        question is a string, answers is a list of pairs. each pair is a 
        possible answer then a boolean of if it's correct.
        e.g
        view.new_question(
          "Is the earth a sphere?", 
          [("yes",True), ("no",False)]
        )
        """

        # put the question on as a label
        question_label = Label(self.parent, text=question)
        question_label.pack()

        # put the answers on as a radio buttons
        var = BooleanVar()
        var.set(False) # initialize
        
        for answer, correct in answers:
            option = Radiobutton(
                self.parent,
                text=answer,
                variable=var,
                value=correct
                )
            option.pack()

        
    def main_loop(self):
        mainloop()

    def register(self, controller):
        """ Register a controller to give callbacks to. """
        self.controller = controller

#==============================================================================
class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.register(self)
        q_and_a = self.model.question_and_answer();
        self.view.new_question(q_and_a[0], q_and_a[1])
        
    def answer(self):
        pass

#==============================================================================
if (__name__ == "__main__"):
    # Note: The view should not send to the model but it is often useful
    # for the view to receive update event information from the model. 
    # However you should not update the model from the view.

    view = View()
    model = Model()
    controller = Controller(model, view)

    view.main_loop()
    
