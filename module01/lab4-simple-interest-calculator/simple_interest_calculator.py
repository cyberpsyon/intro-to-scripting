# Author: Ben Mickens
# Date: 10-30-2025
# Function: This program helps users estimate how much interest they would earn from a basic savings account or investment.

# Gather principal from user and validate
while True:
    try:
        principal = float(input("Enter the principal amount: $"))
        break
    except ValueError:
        print("Enter a valid dollar amount.")

# Gather rate from user and validate
while True:
    try:
        rate = float(input("Enter rate (%): "))
        break
    except ValueError:
        print("Enter a valid number.")

# Gather time from user and validate
while True:
    try:
        time = int(input("Enter time (in months): "))
        if time > 0:
            break
        else:
            print("Please enter time as a whole number greater than 0.")
    except ValueError:
        print("Enter a valid number.")

print(f"The simple interest is ${(principal * rate * time)/100:.2f}.")


