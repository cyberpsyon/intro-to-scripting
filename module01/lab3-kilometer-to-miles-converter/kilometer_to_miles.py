# Author: Ben Mickens
# Date: 10-28-2025
# Function: This program takes input (distance in kilometers) from the user and applies a simple multiplication to give a result in miles.

# Get temp in Fahrenheit from the user
while True:
    try:
        km_distance = float(input("Enter the distance in kilometers: "))
        break
    except ValueError:
        print("Enter a valid number.")

# Convert the value to miles
miles_distance = km_distance * 0.621371

#Display the result in miles using 2 decimal places
print(f"{km_distance} kilometers is equivalent to {miles_distance:.2f} miles.")