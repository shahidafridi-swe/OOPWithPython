from math import pi

class Shape:
    def __init__(self, name ) -> None:
        self.name= name
        
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
        
    def area(self):
        return pi * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, name, land, height) -> None:
        self.land = land
        self.height = height
        super().__init__(name)
        
    def area(self):
        return 0.5 * self.land * self.height
        
rect = Rectangle('rect', 5,5)
cir  = Circle("cir", 5)
tri = Triangle("tri", 5,5)

print(rect.area())
print(cir.area())
print(tri.area())