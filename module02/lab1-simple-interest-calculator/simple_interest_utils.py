# Author: Ben Mickens
# Date: 11-01-2025
# Function: This module provides various functions for Simple Interest Calculation


def get_principal():
    """Get and validate principal amount from user."""
    while True:
        try:
            principal = float(input("Enter the principal amount: $"))
            if principal > 0:
                return principal
            else:
                print("Please enter a principal amount greater than 0.")
        except ValueError:
            print("Enter a valid dollar amount.")


def get_rate():
    """Get and validate interest rate from user."""
    while True:
        try:
            rate = float(input("Enter rate (%): "))
            if rate > 0:
                return rate
            else:
                print("Please enter a rate greater than 0.")
        except ValueError:
            print("Enter a valid number.")


def get_time():
    """Get and validate time period from user."""
    while True:
        try:
            time = float(input("Enter time (years): "))
            if time > 0:
                return time
            else:
                print("Please enter time as a number greater than 0.")
        except ValueError:
            print("Enter a valid number.")


def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest based on principal, rate, and time."""
    return (principal * rate * time) / 100


def get_continue_response():
    """Ask user if they want to continue and validate response."""
    while True:
        response = input("Would you like to calculate another interest value? (y/n): ").strip().lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")