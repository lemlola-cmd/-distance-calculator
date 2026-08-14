import math
# This imports the math library so that I can use sqrt.() and pow.()

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

# This is where you input the x and y values.

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("the distance between the two points is:", round(distance, 2))

# This computes the distance and prints it.

