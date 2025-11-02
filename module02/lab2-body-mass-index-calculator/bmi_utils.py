# Author: Ben Mickens
# Date: 11-01-2025
# Function: This module provides various functions for Body Mass Index (BMI) calculation and classification

def convert_lbs_to_kg(pounds):
    return pounds * 0.45359237

def convert_inches_to_meters(inches):
    return inches * 0.0254

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
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
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}.")
    print(f"According to the U.S. Centers for Disease Control and Prevention (CDC), your classification is: {classify_bmi(bmi)}.")

def calculate_optimal_weight(height):
    min_weight_lbs = 18.5 * (height ** 2) / 0.45359237
    min_weight_kg = convert_lbs_to_kg(min_weight_lbs)
    max_weight_lbs = 25 * (height ** 2) / 0.45359237
    max_weight_kg = convert_lbs_to_kg(max_weight_lbs)
    print(f"According to the CDC, the optimal weight for your height is between {min_weight_kg:.2f} kg ({min_weight_lbs:.1f} lbs) and {max_weight_kg:.2f} kg ({max_weight_lbs:.1f} lbs).")
