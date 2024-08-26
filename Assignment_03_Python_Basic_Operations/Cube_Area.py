
side_length = float(input("Enter side length of cube: "))

def cube_surface_area(side_length):
    surface_area = 6*(side_length**2)
    return surface_area

surface_area = cube_surface_area(side_length)

print(f"Area of cube for {side_length} side length is: {surface_area:.2f} aquare units")