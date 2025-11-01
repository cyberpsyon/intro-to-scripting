# Author: Ben Mickens
# Date: 11-01-2025
# Function: This program helps the user calculate the area of a wall, determine the quantity of paint required, and estimate the total expense based on the price per gallon.

import math

# Gather height from user and validate
while True:
    try:
        height = float(input("Enter the height of the wall (ft): "))
        if height > 0:
            break
        else:
            print("Please enter a height greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Gather width from the user and validate
while True:
    try:
        width = float(input("Enter the width of the wall (ft): "))
        if width > 0:
            break
        else:
            print("Please enter a width greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Gather coverage per gallon from the user and validate
while True:
    try:
        coverage = float(input("Enter the coverage per gallon (sq ft): "))
        if coverage > 0:
            break
        else:
            print("Please enter coverage per gallon greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Gather price per gallon from the user and validate
while True:
    try:
        price_per_gallon = float(input("Enter the price per gallon: $"))
        if price_per_gallon > 0:
            break
        else:
            print("Please enter price per gallon greater than 0.")
    except ValueError:
        print("Enter a valid number.")


# Calculate wall_area, gallons_needed, and paint_cost
wall_area = width * height
gallons_needed = math.ceil(wall_area / coverage)
paint_cost = gallons_needed * price_per_gallon

# Output wall_area, gallons_needed, and paint_cost
print(f"Wall area: {wall_area:.2f} sq ft.")
gallon_text = "gallon" if gallons_needed == 1 else "gallons"
print(f"You will need {gallons_needed} {gallon_text} of paint.")
print(f"Total cost: ${paint_cost:.2f}.")