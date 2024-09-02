def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}.")
