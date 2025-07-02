# ✅ STRINGS:
"""
Every string that we create has a special unicode.

a = 'Hey'
print(ord(a)) --> this is how we check the unicode of any string.

We can also convert unicodes into strings

a = 65
print(chr(a))  --> this is how we convert unicode into characters.
"""

# ✅ STRING INDEXING:
name = "Shakeeb ur Rehman" 
print(name[2])  # --> a


# ✅ STRIG SLICING:
"""
Slicing means cutting out a slice from the string means the small portion.
So for this we have start,stop and step

cris = "Ronaldo"
print(cris[1:-1])

-->  [start:stop:step]
"""


# ✅ TYPE CONVERSION:
"""
For converting a type of variable into another we use some followings functions and this method
is called type conversion
"""

#  ✅ 1. Implicit Type Conversion (Automatic)
""" 
Python automatically converts a smaller data type to a larger data type to avoid data loss.
x = 10      # int
y = 2.5     # float

result = x + y   # x is automatically converted to float
print(result)    # 12.5
print(type(result))  # <class 'float'>
"""



# ✅ 2. Explicit Type Conversion (Type Casting)
"""
You manually convert one data type to another using functions like:

✅ Function	       ✅ Converts to
int()	                Integer
float()	           Floating point number
str()	                String
list()	                 List
tuple()	                Tuple
set()                  	 Set
dict()          Dictionary (from pairs)
"""