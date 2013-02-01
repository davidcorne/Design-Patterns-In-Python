#!/usr/bin/env python
# Written by: DGC

# Inspiration
# http://www.codeproject.com/Articles/25057/Simple-Example-of-MVC-Model-View-Controller-Design
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
        return (key, [x[0] for x in self.q_and_a[key]])

    def is_correct(self, question, answer):
        answers = self.q_and_a[question]
        for ans in answers:
            if (ans[0] == answer):
                return ans[1]
        assert False, "Could not find answer."

#==============================================================================
class View(object):

    def __init__(self):
        self.parent = Tk()

        self.initialise_frame()

        self.controller = None

    def initialise_frame(self):
        self.frame = Frame(self.parent)
        self.frame.pack()

    def new_question(self, question, answers):
        """ 
        question is a string, answers is a list of strings
        e.g
        view.new_question(
          "Is the earth a sphere?", 
          ["Yes", "No"]
        )
        """
        # clear the screen
        self.frame.destroy()
        self.initialise_frame()

        # cache the question
        self.question = question

        # put the question on as a label
        question_label = Label(self.frame, text=self.question)
        question_label.pack()

        # put the answers on as a radio buttons
        self.selected_answer = StringVar()
        self.selected_answer.set(answers[0])

        for answer in answers:
            option = Radiobutton(
                self.frame,
                text=answer,
                variable=self.selected_answer,
                value=answer,
                )
            option.pack()

        # new button to confirm
        button = Button(self.frame, text="Answer", command=self.answer)
        button.pack()
        
    def main_loop(self):
        mainloop()

    def register(self, controller):
        """ Register a controller to give callbacks to. """
        self.controller = controller

    def answer(self):
        self.controller.answer(self.question, self.selected_answer.get())

#==============================================================================
class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.register(self)
        q_and_a = self.model.question_and_answer()
        print(q_and_a)
        self.view.new_question(q_and_a[0], q_and_a[1])
        
    def answer(self, question, answer):
        correct = self.model.is_correct(question, answer)
        print(correct)

        print(
            "We asked: \"" + 
            question + 
            "\", you answered: \"" +
            answer + 
            "\""
            )


#==============================================================================
if (__name__ == "__main__"):
    # Note: The view should not send to the model but it is often useful
    # for the view to receive update event information from the model. 
    # However you should not update the model from the view.

    view = View()
    model = Model()
    controller = Controller(model, view)

    view.main_loop()
    
