# ✅ OBJECTS:
"""
Initializing the class to any variables creates objects.
We can create many objects of a single class.
Object has all the powers to access the attributes and methods of any class.
"""

class Factory:
    name = 'Bag'

    def creat_bag(self):
        print('Your Bag is being create')

# This is how we create objects of any class
bag1 = Factory()
bag2 = Factory()


# ✅ CONSTRUCTOR:
"""
A constructor is a special method that class automatically everytime when
we create object of class.
"""
class Person:
    # this is constructor.
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def greet(self):
        print(F'{self.name} Good Moring.')


boy1 = Person('Shakeeb',23,'Male')
boy1.greet()
        