# you are going to painting a wall . where 1 CAN of paint cover 5  square meter of wall .
# give random height and width of wall
# calculate how many cans of pain you'll need to buy.
# number of cans = (wall width * wall height ) /coverage per can
#e.g. height = 2, width = 4, coverage = 5
# number of cans (2*4)/5 = 1.6
# but you can't buy .6 of can of paint,the result should be round up to 2 can

import math
def paint_calc(height,width,cover):
    area  =  test_h * test_w
    no_of_cans = math.ceil( area / 5 )
    # print(no_of_can_of_paint)
    print(f"you'll need {no_of_cans} cans of paint for wall")

test_h = int(input("enter the wall height: "))
test_w = int(input("enter the wall width: "))
#coverage = 5
paint_calc(height = "test_h",width = "test_w",cover = "coverage")