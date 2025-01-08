# -*- coding: utf-8 -*-
"""py_basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t4iHIFM1TQZFPC3udIJ6vT40u8wEbC2T

# Lists
"""

import numpy

list = [1.6, 'abc',4]
print(list)

#unordered list
list = [10, 30, 20, 40]
print(list)

"""# list operations

**Concatenation**
"""

a = [1, 2, 3]
b = [5, 6, 7]
c = a + b
print(c)

"""**repeatation**"""

a = [0] * 5
print(a)

"""**slicing**"""

a = [1,2,3,4,5,6,7]
print(a[1:3])
print(a[-4:-2])
print(a[-1:-3])
print(a[:5])
print(a[4:])
print(a[:])
print(a)

"""**assignement**"""

age = [18, 19, 20, 16]
hrs_studied = [5, 6, 4, 3.5]
marks =

"""**list cloning**"""

a = [1, 'vivek', 2, 'hari']
b = a[:]
print(b)

"""# data types in py
# 6/1/25
"""

#int
my_int = 42
print("Original Integer: ", my_int)

#list
my_list = [1, 'hello', 3.14, True]
print("Original List: ", my_list)
my_list.append('world')
print("List after appending: ", my_list)
my_list.remove(3.14)
print("List after removing: ", my_list)

#Tuple
my_tuple = (1, 'apple', 3.14, False)
print("Original Tuple: ", my_tuple)
print("Tuple length: ", len(my_tuple))
print("First element of the tuple: ", my_tuple[0])
print("Last element of the tuple: ", my_tuple[-1])

#for loop
for i in range(1,6):
    print(i)

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1111111112

#if condition
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#function
def greet(name):
    print("Hello, " + name + "!")
greet("VIVEK")

"""# Functions in python
# 7/1/25
"""

#function
def greet(name):
    print(f"Hello, " + name + "!")
greet("VIVEK")

#to get all the built-in functions in python
print(dir(str))

"""# Methods"""

#lower to upper
a = "hello world"
b = a.upper()
print(b)

#upper to lower
a = "HELLO WORLD"
b = a.lower()
print(b)

#title case
a = "hello world"
b = a.title()
print(b)

#replace
a = "hello world"
b = a.replace('hello', 'hi')
print(b)

#isdigit method( returns boolean[ checks whether the provided value is boolean or not])
a = "hello world"
b = a.isdigit()
print(b)

a = "1234"
b = a.isdigit()
print(b)

a = "1234abc"
b = a.isdigit()
print(b)

#range function
a = range(5)
print(a)

a = range(5)
print(list(a))

#start, stop, then steps
my_list = list(range(5, 15, 2))
print(my_list)

#function with returns
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)

#functions with default values
def greet(name="VIVEK", greeting="Hello"):
    print({greeting}, {name})
    greet()

#function with *args
def print_sum(*args):
    total = sum(args)
    print("The sum is:", total)
print_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

#creating a program and adding 2 more functions to it
#providiing pre defined username and password
right_username = 'admin'
right_password = '0000'
while True:
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == right_username and password == right_password:
    print("Login Successful. WELCOME!!!")
    break
  else:
    print("Login Failed!.Invalid username or Password!!.Please try again!!!")

# Task using method, user defined function and builtin function
# Method
a = '1233456'
b = a.isnumeric()
print(b)

#builtin function
a = [34, 45, 63, 72, 10]
b = max(a)
print(b)

#user defined function
def interest_calculator(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
principal = 10000
rate = 5
time = 2
interest = interest_calculator(principal, rate, time)
print(f"The calculated interest is: {interest}")