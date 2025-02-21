import math
import sys

def calc_area(r):
    area = math.pi*r**2
    return area

# Cálculo del área del círculo
radius = 5 
Area = calc_area(radius) 
print(f"Area of circle: {Area}")
