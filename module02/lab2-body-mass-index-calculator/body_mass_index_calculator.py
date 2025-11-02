# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program utilizes modularity and a menu to calculate a user's Body Mass Index (BMI)

import bmi_utils as b

def main():
    print("Welcome to the BMI Calculator!")
    while True:
        print("\nChoose an option:")
        print("1) Convert weight in pounds (lbs) to kilograms (kg)")
        print("2) Convert height in inches (in) to meters (m)")
        print("3) Calculate BMI")
        print("4) Calculate optimal weight")
        print("5) Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            pounds = float(input("Enter your weight in pounds (lbs): "))
            print(f"Your weight in kilograms (kg) is {b.convert_lbs_to_kg(pounds):.2f}.")
        elif choice == "2":
            inches = float(input("Enter your height in inches (in): "))
            print(f"Your height in meters (m) is {b.convert_inches_to_meters(inches):.2f}.")
        elif choice == "3":
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            bmi = b.calculate_bmi(weight, height)
            b.output_bmi_stats(bmi)
        elif choice == "4":
            height = float(input("Enter your height in meters (m): "))
            b.calculate_optimal_weight(height)
        elif choice == "5":
            print("Thank you for using BMI Calculator!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()