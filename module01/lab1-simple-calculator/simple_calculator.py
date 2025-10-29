# Author: Ben Mickens
# Date: 10-26-2025
# Function: This program takes in two numbers from the user and return the result of adding, subtracting, multiplying, and dividing those numbers.

# Get and validate first number
while True:
    try:
        num1 = int(input("Enter first number: "))
        break
    except ValueError:
        print("Please enter a number.")

# Get and validate second number
while True:
    try:
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter a number.")

# Add
print(f"{num1} + {num2} = {num1 + num2}")

# Difference
print(f"{num1} - {num2} = {num1 - num2}")

# Product
print(f"{num1} * {num2} = {num1 * num2}")

# Quotient
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"Cannot divide {num1} by 0")