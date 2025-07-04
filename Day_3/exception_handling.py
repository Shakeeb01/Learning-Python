# This program asks the user to enter a number and divides 100 by that number.
# It handles common exceptions like ZeroDivisionError and ValueError.

try:
    # Ask user to enter a number
    user_input = input("Enter a number to divide 100: ")
    
    # Try to convert the input to an integer
    number = int(user_input)
    
    # Try to divide 100 by the entered number
    result = 100 / number

except ZeroDivisionError:
    # This block runs if the user enters 0
    print("Error: You cannot divide by zero.")

except ValueError:
    # This block runs if the input is not a valid integer (e.g., a letter or symbol)
    print("Error: Please enter a valid integer.")

else:
    # This block runs only if no exception occurs
    print("Success! The result is:", result)

finally:
    # This block always runs, no matter what
    print("Thank you for using the division program.")
