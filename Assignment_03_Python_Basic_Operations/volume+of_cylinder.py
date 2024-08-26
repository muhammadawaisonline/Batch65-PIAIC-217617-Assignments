import math

def calculate_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Example usage
radius = float(input("Enter the radius of the cylinder (in meters): "))
height = float(input("Enter the height of the cylinder (in meters): "))

volume = calculate_volume(radius, height)
print(f"The volume of the cylinder is {volume:.2f} cubic meters.")
