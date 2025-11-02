# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program computes simple interest for customers based on the principal amount, annual interest rate, and the number of years.
# Note: This program expands on the Module 1 Simple Interest Calculator by adding functions and loops to allow the user to calculate multiple interest values.

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


def main():
    """Main function to run the simple interest calculator."""
    print("Welcome to the Simple Interest Calculator!")
    print()

    while True:
        # Get input from user
        principal = get_principal()
        rate = get_rate()
        time = get_time()

        # Calculate and display interest
        interest = calculate_simple_interest(principal, rate, time)
        print(f"The simple interest is ${interest:.2f}.")
        print()

        # Check if user wants to continue
        if not get_continue_response():
            print("Thank you for using the Simple Interest Calculator!")
            break


# Run the program
if __name__ == "__main__":
    main()