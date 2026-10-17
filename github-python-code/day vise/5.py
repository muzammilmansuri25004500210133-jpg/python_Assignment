import math

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

area = l * b
perimeter = 2 * (l + b)

circle_area = math.pi * l * l

print("Rectangle Area =", area)
print("Rectangle Perimeter =", perimeter)
print("Circle Area =", circle_area)