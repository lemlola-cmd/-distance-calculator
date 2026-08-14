import math

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("the distance between the two points is:", distance)

# Using a library is more practical and easier than making something from scratch because, making something from scratch is long and tiresome, having to go to trial and error if you get it wrong. 