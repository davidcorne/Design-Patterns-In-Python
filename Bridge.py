#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Shape(object):

    def __init__(self):
        self.calculator = None

    def area(self):
        """ 
        Returns the area of the shape calculated using the shape specific 
        implementation. 
        """
        assert self.calculator != None, "self.calculator not defined."
        return self.calculator.calculate()

#==============================================================================
class Rectangle(Shape):
    
    def __init__(self, x, y):
        self.calculator = RectangleAreaImpl(x, y)
        self.x = x
        self.y = y

#==============================================================================
class RectangleAreaImpl(object):

  def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        return self.x * self.y
 
#==============================================================================
class Triangle(Shape):

    def __init__(self, base, height):
        self.calculator = TriangleAreaImpl(base, height)
        self.base = base
        self.height = height

#==============================================================================
class TriangleAreaImpl(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        return 0.5 * self.base * self.height
       
#==============================================================================
if (__name__ == "__main__"):
    rect = Rectangle(4, 5)
    print("4 x 5 Rectangle area: %d" %(rect.area()))
  
    tri = Triangle(4.0, 5.0);
    print("Base 4 height 5 Triangle area: %d" %(tri.area()))
