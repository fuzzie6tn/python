#area of wall
import math
def paint_calc(height,width,cover):
    area = height*width
    num_can = math.ceil(area/cover)
    print(f"You will need {num_can} of cans")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width=test_w, cover=coverage)