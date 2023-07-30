import math




def area_of_square(side_length):
    # Calculate the area of a square
    area = side_length ** 2
    return area

def area_of_circle(radius):
    # Calculate the area of a circle
    area = math.pi * radius ** 2
    return area

def area_of_rectangle(length, width):
    # Calculate area of a rectangle
    area = length * width
    return area

def area_of_cylinder(radius, height):
    # Calculate the lateral surface area of a cylinder
    lateral_area = 2 * math.pi * radius * height
    # Calculate the base area of the cylinder
    base_area = math.pi * radius ** 2
    # Calculate the total surface area of the cylinder
    total_area = 2 * base_area + lateral_area
    return total_area

def area_of_triangle(base, height):
    # Calculate the area of a triangle
    area = 0.5 * base * height
    return area
def area_of_polygons(sides_num, side_length):

    # Calculate the area of a polygon
    area = (sides_num * side_length ** 2) / (4 * math.tan(math.pi / sides_num))
    return area

def display_menu():
    print("Enter number from 1-6")
    print("1. Area of Square")
    print("2. Area of Circle")
    print("3. Area of Rectangle")
    print("4. Area of Cylinder")
    print("5. Area of Triangle")
    print("6. Area of Polygon")

while True:
    display_menu()
    choice = input("Choose a number or type quit : ")

    if choice.lower() == 'quit':
        break

    if choice == '1':
        side_length = int(input("Enter the side length of the square: "))
        area = area_of_square(side_length)
    elif choice == '2':
        radius = int(input("Enter the radius of the circle: "))
        area = area_of_circle(radius)
    elif choice == '3':
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = area_of_rectangle(length, width)
    elif choice == '4':
        radius = int(input("Enter the radius of the cylinder: "))
        height = int(input("Enter the height of the cylinder: "))
        area = area_of_cylinder(radius, height)
    elif choice == '5':
        base = int(input("Enter the base length of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        area = area_of_triangle(base, height)
    elif choice == '6':
        side_length = int(input("Enter the base length of the Polygon: "))
        sides_num = int(input(f"Enter the height of the Polygon: "))
        area = area_of_polygons(sides_num,side_length)
    else:
        print("Invalid choice. Please select a valid number or enter 'quit' to exit.")
        continue

    print(f"The area is: ",area)
