import math

def compare(x, y):
	if x > y:
		return 1
	elif x < y:
		return -1
	else:
		return 0

print(compare(2, 3))
print(compare(2, 2))
print(compare(3, 2))

def hypotenuse(a, b):
	return math.sqrt(a**2 + b**2)
	
print(hypotenuse(3,4))

def is_between(x, y, z):
	return x <= y and y <= z
	
print(is_between(2,3,4))
print(is_between(2,3,1))