
def is_power(a, b):
	if a == 1:
		return True
	elif a % b == 0:
		return is_power(a/b, b)
	else: 
		return False
	
#a is a power of b if it is divisible by b
#a/b is a power of b

print(is_power(9, 3))
print(is_power(25, 5))
print(is_power(1024, 2))
print(is_power(36, 4))