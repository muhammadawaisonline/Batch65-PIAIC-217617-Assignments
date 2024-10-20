import math

radius = float(input("Enter radius of circle: "))

def circle_area(radius):
    area = math.pi*radius*radius

    return round(area, 2)

area = circle_area(radius)

print(f"Area of circle is {area} square units")

""" print(f"Area of circle is {area:.2f} square units") """