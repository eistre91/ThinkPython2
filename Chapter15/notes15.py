import math

class Point:
	"""Represents a point in 2-D space.
	
	attributes:x, y
	"""
	
def distance_between_points(p1, p2):
	return math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 )
	
class Rectangle:
	"""Represents a rectangle.
	
	attributes: width, height, corner.
	"""

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

p1 = Point()
p1.x = 3.0
p1.y = 4.0
import copy
p2 = copy.copy(p1)
#there's also copy.deepcopy for getting at objects
#inside objects