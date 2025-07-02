# ✅ CONDITIONAL STATEMENTS:
""" 
Conditional statements in Python are used to perform different actions based on different conditions. They allow your program to make decisions.
"""

# ✅ EXAMPLE:
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")



# ✅ NESTED STATEMENTS:
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Access granted.")
    else:
        print("ID required.")
else:
    print("You are underage.")




# ✅ LOGICAL OPERATORS IN CONDITIONS:
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")
else:
    print('Sorry You Can not enter.')