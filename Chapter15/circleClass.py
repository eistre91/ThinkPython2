import math

class Point:
	"""Represents a point.
	
	attributes:x, y"""

class Circle:
	"""Represents a circle.
	
	attributes: center, radius"""
	
class Rectangle:
	"""Represents a rectangle.
	
	attributes: width, height, corner.
	"""
	
center = Point()
center.x = 150
center.y = 100
cir1 = Circle()
cir1.center = center
cir1.radius = 75

rect1 = Rectangle()
corner = Point()
corner.x = 125
corner.y = 125
rect1.corner = corner
rect1.width = 10
rect1.height = 10

def distance_between_points(p1, p2):
	return math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 )

def point_in_circle(cir, p):
	return distance_between_points(cir.center, p) <= 75
	
def rect_in_circle(cir, rect):
	top_right = Point()
	top_right.x = rect.corner.x + rect.width
	top_right.y = rect.corner.y + rect.height
	return distance_between_points(cir.center, top_right) <= 75 and \
			distance_between_points(cir.center, rect.corner) <= 75

def rect_circle_overlap(cir, rect):
	top_right = Point()
	top_right.x = rect.corner.x + rect.width
	top_right.y = rect.corner.y + rect.height
	top_left = Point()
	top_left.x = rect.corner.x
	top_left.y = rect.corner.y + rect.height
	bottom_right = Point()
	bottom_right.x = rect.corner.x + rect.width
	bottom_right.y = rect.corner.y 
	return distance_between_points(cir.center, top_right) <= 75 or \
			distance_between_points(cir.center, rect.corner) <= 75 or \
			distance_between_points(cir.center, top_left) <= 75 or \
			distance_between_points(cir.center, bottom_right) <= 75
	
print(point_in_circle(cir1, center))
print(rect_in_circle(cir1, rect1))
print(rect_circle_overlap(cir1, rect1))