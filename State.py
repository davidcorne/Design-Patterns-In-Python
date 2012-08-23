#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Language(object):
    
    def __init__(self):
        self.hello = ""

    def greet(self):
        return self.hello

#==============================================================================
class English(Language):
    
    def __init__(self):
        self.hello = "Hello"

#==============================================================================
class French(Language):
    
    def __init__(self):
        self.hello = "Bonjour"

#==============================================================================
class Spanish(Language):
    
    def __init__(self):
        self.hello = "Hola"

#==============================================================================
class Multilinguist(object):

    def __init__(self, language):
        self.language = language

    def greet(self):
        print(self.language.greet())

#==============================================================================
if (__name__ == "__main__"):

    translator = Multilinguist(English())
    translator.greet()

    translator.language = French()    
    translator.greet()

    translator.language = Spanish()    
    translator.greet()
