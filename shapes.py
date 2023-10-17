import math 

def area_and_perimeter_circle (radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def area_and_perimeter_rectangle (length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def area_and_perimeter_square (side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

def area_and_perimeter_triangle (side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    perimeter = side1 + side2 + side3
    return area, perimeter

print("1. Circle")  
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area, perimeter = area_and_perimeter_circle(radius)
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area, perimeter = area_and_perimeter_rectangle(length, width)
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

elif choice == 3:
    side = float(input("Enter side: "))
    area, perimeter = area_and_perimeter_square(side)
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

elif choice == 4:
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    area, perimeter = area_and_perimeter_triangle(side1, side2, side3)
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

else:
    print("Invalid choice")

