# ✅ LOOPS:
"""
Loops in python allow us to execute a block of code multiple times without rewriting it.
There are two types of loops in python.
1. For Loop
2. While Loop
"""


# ✅ FOR LOOP:
"""
In for loop we almost everytime we use a range function which takes three things.
range(S,S,S)  -> three 'S' means Start,Stop and Step
In range function we have default value of 0 for the start 
and have default value of 1 for step.
"""

# ✅ FOR LOOP SYNTAX:
for i in range(1,10,1):
    print(i)



# ✅ REVERSE FOR LOOP:
for j in range(10,0,-1):
    print(j)



# ✅ LOOPS FOR STRING:
a = "Shakeeb"
for i in range(len(a)):
    print(i)       # --> This will index from 0 to onward.
    print(a[i])    # --> This will value from S to onward.




# ✅ FOR LOOPS QUESTIONS:

# 1️⃣ Accept an integer and print hello world n time.
n = int(input('Enter the number: '))
for i in range(n):
    print('Hello World')



# 2️⃣ Print natural numbers up to n
n = int(input('Enter the number: '))
for i in range(0,n+1):
    print(i)




# 3️⃣ Take the number from user and prints it's tabel.
n = int(input('Enter the number: '))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')



# 4️⃣ Sum up to n terms
n = int(input('Enter the number: '))
sum = 0
for i in range(1,n+1):
    sum += i

print(f'Sum of you number is {sum}')



# 5️⃣ Factorial of number.
n = int(input('Enter the number: '))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(f'Sum of you number is {factorial}')


# 6️⃣ Reverse the string
str = 'Shakeeb'

reverse_str = ''

for i in range(len(str) -1,-1,-1):
    reverse_str += str[i]

print(reverse_str)



# ✅ WHILE LOOPS & QUESTIONS:

print('Guess the number between 1 to 6 in three tries.')
a = 1
while a <= 3:
    guess = int(input('Enter Your Guess: '))
    if guess == 4:
        print('You Won')
        break
    else:
        print('Try AGAIN')
    a+=1