#Area of polygn
import math

def area_of_polygon(num_sides, side_length):

    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    return area


num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the side: "))

area = area_of_polygon(num_sides, side_length)
print(f"The area of the polygon is: ",area)