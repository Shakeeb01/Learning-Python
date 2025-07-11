# ✅ OOP:
"""
OOP stands for object oriented programming.
This is the separate style of programming in which we deals with classes and objects.
"""

# ✅ CLASSES:
"""
A class is like a blue print or template for creating objects.
We can create as many as we want objects from single class.

There are two types of things in class:
1. Attributes - Variables defined inside the class
2. Methods    - Functions defined inside the class

"""
# ✅ SYNTAX OF CLASS:
class Animal:
    species = 'Dog'  # Attributes

    def make_sound(self):
        print('Wao')   # Method


# ✅ Accessing Class Attributes and methods:
Animal().species
Animal.make_sound()