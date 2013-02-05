#!/usr/bin/env python
# Written by: DGC

# python imports

# local imports
from test import *
import MVC

#==============================================================================
class utest_MVC(UnitTest):
    
    def __init__(self):
        super(utest_MVC, self).__init__()

    def model_test(self):
        model = MVC.Model()
        question, possible_answers = model.question_and_answers()

        # can't test what they are because they're random
        test(isinstance(question, str), "Question should be a string")
        test(isinstance(possible_answers, list), "Answers should be a list")

        for item in possible_answers:
            test(
                isinstance(item[0], str),
                "Elements of possible answer list should be strings"
                )

    def controller_test(self):
        model = ModelMock()
        view = ViewMock()
        controller = MVC.Controller(model, view)
        controller.new_question()
        test(
            view.question == "Question", 
            "Controller should pass the question to the view."
            )
        controller.answer("Question", "correct")
        test(
            controller.view.mock_feedback == "That is correct.", 
            "The feedback for a correct answer is wrong."
            )
        controller.answer("Question", "incorrect")
        test(
            controller.view.mock_feedback == "Sorry that's wrong.", 
            "The feedback for an incorrect answer is wrong."
            )

#==============================================================================
class ViewMock(object):
    
    def new_question(self, question, answers):
        self.question = question
        self.answers = answers

    def register(self, controller):
        pass

    def feedback(self, feedback):
        self.mock_feedback = feedback

#==============================================================================
class ModelMock(object):
    
    def question_and_answers(self):
        return ("Question", ["correct", "incorrect"])

    def is_correct(self, question, answer):
        correct = False
        if (answer == "correct"):
            correct = True
        return correct

#==============================================================================
if (__name__ == "__main__"):
    utest_MVC()
