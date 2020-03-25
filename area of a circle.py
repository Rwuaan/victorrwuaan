# A program that computes th area of a circle
radius = input("What is the radius of the circle in centimetres? ")
radius = float(radius)
# importing math module
import math
area = math.pi *radius**2
print("The area of the  circle is " + str(area))
