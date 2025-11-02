# Author: Ben Mickens
# Date: 11-01-2025
# Function: This module provides various functions for Body Mass Index (BMI) calculation and classification

def convert_lbs_to_kg(pounds):
    """ Converts weight in pounds to kilograms."""
    return pounds * 0.45359237

def convert_inches_to_meters(inches):
    """ Converts inches to meters."""
    return inches * 0.0254

def calculate_bmi(weight, height):
    """ Calculate BMI based on weight and height."""
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return weight / (height ** 2)

def classify_bmi(bmi):
    """ Classify BMI based on CDC guidelines."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Class 1 Obesity"
    elif bmi < 40:
        return "Class 2 Obesity"
    else:
        return "Class 3 Obesity (Severe Obesity)"

def output_bmi_stats(bmi):
    """ Output BMI stats."""
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}.")
    print(f"According to the U.S. Centers for Disease Control and Prevention (CDC), your classification is: {classify_bmi(bmi)}.")

def calculate_optimal_weight(height):
    """ Calculate optimal weight based on height."""
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
        # Calculate minimum weight (BMI = 18.5)
    min_weight_kg = 18.5 * (height ** 2)
    min_weight_lbs = min_weight_kg / 0.45359237

    # Calculate maximum weight (BMI = 25)
    max_weight_kg = 25 * (height ** 2)
    max_weight_lbs = max_weight_kg / 0.45359237
    print(f"According to the CDC, the optimal weight for your height is between {min_weight_kg:.2f} kg ({min_weight_lbs:.1f} lbs) and {max_weight_kg:.2f} kg ({max_weight_lbs:.1f} lbs).")
