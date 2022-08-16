#Calculate the amount of paint needed to make a paint wall

import math

def paint_calc(height, width, cover):
    """
    Calculate the amount of paint needed to make a paint wall
    """
    area = (math.ceil((height * width)/cover))

    print (f"You'll need {area} cans of paint")



test_h = int(input("Enter the height of the wall: "))
test_w = int(input("Enter the width of the wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)