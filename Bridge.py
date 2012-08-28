#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Shape(object):

    def __init__(self):
        # fakes an abstract base class in Python 2
        raise NotImplementedError

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
    x = 4
    y = 5
    rect = Rectangle(x, y)
    print(str(x) + " x " + str(y) + " Rectangle area: " + str(rect.area()))
  
    base = 4
    height = 5
    tri = Triangle(base, height);
    print(
        "Base " +
        str(base) +
        ", Height " +
        str(height) + 
        " Triangle area: " +
        str(tri.area())
        )
