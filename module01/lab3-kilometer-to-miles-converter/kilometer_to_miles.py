# Author: Ben Mickens
# Date: 10-28-2025
# Function: This program takes input (distance in kilometers) from the user and applies a simple multiplication to give a result in miles.

# Get temp in Fahrenheit from the user
while True:
    try:
        kmDistance = float(input("Enter the distance in kilometers: "))
        break
    except ValueError:
        print("Enter a valid number.")

# Convert the value to miles
milesDistance = kmDistance * 0.621371

#Display the result in miles using 2 decimal places
print(f"{kmDistance} kilometers is equivalent to {milesDistance:.2f} miles.")