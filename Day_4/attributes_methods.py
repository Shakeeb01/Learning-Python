# ✅ TYPES OF ATTRIBUTES:
""" 
Attributes are just the variables that defined inside the class.

1. Class Attribute:
    A normal variable created inside the class.
2. Instance Attribute:
    A variable created an instance like self.name or self.age.
"""
class Animal:
    name = 'Dog' # 👈 Class Attribute

    def __init__(self,color):
        self.color = color  # 👈 Instance Attribute




# ✅ TYPES OF METHODS:
"""
Functions that are defined inside the class called Methods.

1. Instance Method:
    An Instance method works with instance(object) of the class.it can access and modify
    instance attributes.these methods take `self` as the first parameter

2. Class Method:
    This method works with the class itself it will not target the instance(object)
    We have to use @classmethod decorator.These Methods takes `cls` as the first parameter

3. Static Method:
    This method does not access class or instance directly it also uses @staticmethod decorator.
    it acts like regular function placed inside a class.
    these Methods do not  takes `self` or `cls` as the first parameter 
"""

class Company:
    # Class variable (shared by all instances)
    total_employes = 10

    def __init__(self, name, role):
        self.name = name          # Instance variable
        self.role = role       # Instance variable

    # 1. Instance Method
    def get_info(self):
        return f"My name is {self.name} and I am a {self.role}."

    # 2. Class Method
    @classmethod
    def get_total_employees(cls):
        return f"Total number of employees: {cls.total_employes}"

    # 3. Static Method
    @staticmethod
    def greet():
        return "Hi You Are Welcome To The Team"


# Create objects
employe1 = Company("Shakeeb", "Backend Developer")
employe2 = Company("Ronaldo", "Frontend Developer")

# Instance method
print(employe1.get_info())       # Output: My name is Shakeeb and I am a Backend Developer.

# Class method
print(Company.get_total_employees())  # Output: Total number of employees: 10

# Static method
print(Company.greet())            # Hi You Are Welcome To The Team
