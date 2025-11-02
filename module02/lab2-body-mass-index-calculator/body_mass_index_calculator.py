# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program utilizes modularity and a menu to calculate a user's Body Mass Index (BMI)

import bmi_utils as b

def main():
    """ Main entry point of the program."""
    print("Welcome to the BMI Calculator!")
    while True:
        # Display menu
        print("\nChoose an option:")
        print("1) Convert weight in pounds (lbs) to kilograms (kg)")
        print("2) Convert height in inches (in) to meters (m)")
        print("3) Calculate BMI")
        print("4) Calculate optimal weight")
        print("5) Exit")

        choice = input("Enter your choice (1-5): ")

        # Convert pounds to kilograms
        if choice == "1":
            try:
                pounds = float(input("Enter your weight in pounds (lbs): "))
                if pounds <= 0:
                    raise ValueError("Weight must be greater than zero")
                else:
                    print(f"Your weight in kilograms (kg) is {b.convert_lbs_to_kg(pounds):.2f}.")
            except ValueError as e:
                if "must be greater than zero" in str(e):
                    print(str(e))
                else:
                    print("Please enter a valid number.")
        # Convert inches to meters
        elif choice == "2":
            try:
                inches = float(input("Enter your height in inches (in): "))
                if inches <= 0:
                    raise ValueError("Height must be greater than zero")
                else:
                    print(f"Your height in meters (m) is {b.convert_inches_to_meters(inches):.2f}.")
            except ValueError as e:
                if "must be greater than zero" in str(e):
                    print(str(e))
                else:
                    print("Please enter a valid number.")
        # Calculate BMI
        elif choice == "3":
            try:
                weight = float(input("Enter your weight in kilograms (kg): "))
                height = float(input("Enter your height in meters (m): "))
                if weight <= 0 or height <= 0:
                    raise ValueError("Height and weight must be greater than zero")
                else:
                    bmi = b.calculate_bmi(weight, height)
                    b.output_bmi_stats(bmi)
            except ValueError as e:
                if "must be greater than zero" in str(e):
                    print(str(e))
                else:
                    print("Please enter a valid number.")
        # Calculate optimal weight range
        elif choice == "4":
            try:
                height = float(input("Enter your height in meters (m): "))
                if height <= 0:
                    raise ValueError("Height must be greater than zero")
                else:
                    b.calculate_optimal_weight(height)
            except ValueError as e:
                if "must be greater than zero" in str(e):
                    print(str(e))
                else:
                    print("Please enter a valid number.")
        # Exit the program
        elif choice == "5":
            print("Thank you for using BMI Calculator!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()