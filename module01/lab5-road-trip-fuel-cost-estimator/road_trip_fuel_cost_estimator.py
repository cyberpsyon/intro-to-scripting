# Author: Ben Mickens
# Date: 10-31-2025
# Function: This program calculates estimated fuel cost based on the distance, the car's fuel efficiency, and the current gas price.

# Gather distance from user and validate
while True:
    try:
        distance = float(input("Enter the distance of your trip (miles): "))
        if distance > 0:
            break
        else:
            print("Please enter a distance greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Gather fuel efficiency from user and validate
while True:
    try:
        fuel_efficiency = float(input("Enter your vehicles fuel efficiency (MPG): "))
        if fuel_efficiency > 0:
            break
        else:
            print("Please enter fuel efficiency as a number greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Gather gas price from user and validate
while True:
    try:
        gas_price = float(input("Enter the current gas price per gallon: $"))
        if gas_price > 0:
            break
        else:
            print("Please enter gas price as a dollar amount greater than 0.")
    except ValueError:
        print("Enter a valid number.")

# Calculate total gas and fuel cost needed for the trip
total_gas = distance / fuel_efficiency
fuel_cost = total_gas * gas_price

# Output total gas and fuel cost
print(f"You will need {total_gas:.2f} gallons of gas.")
print(f"The total cost of fuel will be ${fuel_cost:.2f}.")