# Author: Ben Mickens
# Date: 10-26-2025
# Function: This program asks the user for a temperature in Fahrenheit, converts it to Celsius, and displays the result with precision.

# Get temp in Fahrenheit from the user
while True:
    try:
        fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
        break
    except ValueError:
        print("Enter a valid number.")

# Convert to Celsius
celsius_temp = (5/9)*(fahrenheit_temp-32)

# Output converted temperature
print(f"The temperature in Celsius is {celsius_temp:.2f} degrees Fahrenheit.")
if fahrenheit_temp > 80:
    print("It's shorts and T-shirt weather!")
elif fahrenheit_temp > 65:
    print("Bring a jacket!")
elif fahrenheit_temp > 50:
    print("It's going to be chilly!")
elif fahrenheit_temp > 32:
    print("Bundle up and don't forget your chapstick!")
else:
    print("Get the sled dogs ready!")