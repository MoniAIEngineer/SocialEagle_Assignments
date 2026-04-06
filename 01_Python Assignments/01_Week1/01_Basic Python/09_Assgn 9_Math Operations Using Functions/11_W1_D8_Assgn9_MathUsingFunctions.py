'''
***************************************************
Assignment No:9 - Test a Math function Add, Sub, 
Mul, Divide and Factorial using Functions
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj
***************************************************
'''
# Import factorial function from math module
import math

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

# Function for factorial
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    else:
        return math.factorial(n)

# Example usage
num1 = 10
num2 = 5
num3 = 4  # For factorial

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print(f"Factorial of {num3}:", factorial(num3))