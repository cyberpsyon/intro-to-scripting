# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program computes simple interest for customers based on the principal amount, annual interest rate, and the number of years.
# Note: This program expands on the Module 1 Simple Interest Calculator by adding a while loop allow the user to calculate multiple interest values.
while True:
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
                time = float(input("Enter time (years): "))
                if time > 0:
                    break
                else:
                    print("Please enter time as a whole number greater than 0.")
            except ValueError:
                print("Enter a valid number.")
        # Output calculated interest
        print(f"The simple interest is ${(principal * rate * time)/100:.2f}.")

        # Ask if user wants to continue with validation
        while True:
            response = input("Would you like to calculate another interest value? (y/n): ").strip().lower()
            if response == "y":
                break
            elif response == "n":
                print("Thank you for using the Simple Interest Calculator!")
                exit()  # Exit the program
            else:
                print("Please enter 'y' for yes or 'n' for no.")