
def check_triangle(a, b, c):
	if a > (b + c):
		print("No")
	elif b > (a + c):
		print("No")
	elif c > (a + b):
		print("No")
	else:
		print("Yes")
		
def input_lengths():
	a = input("Side 1 length?")
	b = input("Side 2 length?")
	c = input("Side 3 length?")
	check_triangle(int(a), int(b), int(c))
	
input_lengths()