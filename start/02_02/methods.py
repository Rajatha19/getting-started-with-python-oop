"""
Python class methods
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def display(self):
        print(f"area:{self.base*self.height}")


new_rectangle = Rectangle(12, 10)
new_rectangle.display()