# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program computes simple interest for customers based on the principal amount, annual interest rate, and the number of years.
# Note: This program expands on the Module 1 Simple Interest Calculator by adding modular functions.

import simple_interest_utils as si

def main():
    """Main function to run the simple interest calculator."""
    print("Welcome to the Simple Interest Calculator!")
    print()

    while True:
        # Get input from user
        principal = si.get_principal()
        rate = si.get_rate()
        time = si.get_time()

        # Calculate and display interest
        interest = si.calculate_simple_interest(principal, rate, time)
        print(f"The simple interest is ${interest:.2f}.")
        print()

        # Check if user wants to continue
        if not si.get_continue_response():
            print("Thank you for using the Simple Interest Calculator!")
            break

# Run the program
if __name__ == "__main__":
    main()