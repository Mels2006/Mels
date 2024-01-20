# ● Create Point namedtuple
# ● Create two points objects from Point namedtuple
# ● Write a function to get distance between that two points
from collections import namedtuple
import math
Point = namedtuple("Point",['x','y'])
point_1 = Point(x = 11,y = 20)
point_2 = Point(x = 31,y = 41)
def get_distance(point_1,point_2):
    return math.sqrt((point_2.x - point_1.x)**2 + (point_2.y - point_1.y)**2)
ditance = get_distance(point_1,point_2)
print(ditance)


    
        

