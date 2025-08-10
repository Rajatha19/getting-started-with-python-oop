"""
Python Polymorphism example
"""

class ClassA:
    def meme(self):
        print("meme() from class A")
class ClassB(ClassA):
    def meme(self):
        print("meme() from class B") 
a=ClassA()
b=ClassB()
a.meme()
b.meme()

