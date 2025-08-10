"""
A class for representing a circle
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def display_circumference(self):
        print(f"Circumference:{2*3.14*self.radius}")
    def display_area(self):
        print(f"Area:{3.14*self.radius*self.radius}")
new=Circle(2)
new.display_circumference()
new.display_area()