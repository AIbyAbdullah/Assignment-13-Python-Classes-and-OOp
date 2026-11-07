'''
Pillar 4: Abstraction
Q7. Shape Calculator | Beginner
Use ABC and @abstractmethod to define an abstract Shape class with area() and perimeter(). Implement both
methods in Circle and Rectangle. Accept dimensions through constructors and use pi = 3.14159. Test a circle
with radius 5 and a rectangle with width 4 and height 6. Attempt to instantiate Shape directly and explain the
outcome.
'''
from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return  3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    

# --- Demo ---
print("--- Shape Calculator ---")
c1 = circle(5)
print(f"Circle (r={c1.radius}) -> Area : {c1.area():.2f} ,perimeter: {c1.perimeter():.2f}") # ya ({c1.radius}) ko (r=5 bhi likhsakte hai hardcodede)

r1 = Rectangle(4,5)
print(f"Rectangle ({r1.width}x{r1.height}) -> Area: {r1.area()}, Perimeter: {r1.perimeter()}")


# Extension: Attempt to instantiate Shape directly
print("\n--- Trying to create Shape object ---")
try:
    s = shape()
except TypeError as e:
    print(f"Error Aya: {e}")
    print("Wajah: Shape abstract class hai. Iska direct object nahi ban sakta jab tak area() aur perimeter() implement na hon.")