from math import pi
import math as m
import random
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

class Quadrilateral(Shape):
    pass

class Square(Quadrilateral):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

class Rectangle(Quadrilateral):
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.length=length
        self.width=width
        
    def area(self):
        return self.length*self.width    
    
    def diagonal(self):
        return m.sqrt((self.length)**2 + (self.width)**2)
    
    def fact(self):
        print(f"i am rectangle, i am 4 headed. i have 90 angles like square. my lenth= {self.length} my width= {self.width} mydiag= {Rectangle.diagonal(self)}")
    
    def __add__(self,thing):
       return self.area()+thing.area()
        
def childrenchops():
    shapes = []
    for _ in range(3):  # Generate one of each shape
        radius = random.randint(5, 9)
        length = random.randint(5, 9)
        breadth = random.randint(5, 9)

        c=Circle(radius)
        r=Rectangle(length, breadth)
        s=Square(length)
        # Create one instance of each shape
        shapes.append(c)
        shapes.append(r)
        shapes.append(s)  # Length is used for both sides in Square

    return shapes
    
    
if __name__=="__main__":       
    a = Square(4)
    b = Circle(7)
    c = Rectangle(5,12)
    Rectangle.fact(c)
    k=Rectangle(7,24)
    c.fact()
    print(c)
    print(b)
    print(b.fact())
    print(a.fact())
    print(b.area())
    print("-"*20)
    print("sum of area of rectanles is: ",c+k)
