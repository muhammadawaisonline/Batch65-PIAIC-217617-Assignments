

length = float(input("Enter lenth of rectangle in cm: "))
width = float(input("Enter width of rectange in cm: "))


def rectangle_area(length, width):
    area = length*width
    return area

area = rectangle_area(length, width)

print(f"Area of rectangle is: {area} cm square. ")