def check_fermat(a, b, c, n):
	if (a**n + b**n) == c**n and n > 2:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")
		
def input_values():
	a = input("Value for a?")
	b = input("Value for b?")
	c = input("Value for c?")
	n = input("Value for n?")
	check_fermat(int(a), int(b), int(c), int(n))

input_values()