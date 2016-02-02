import math

#y = ( x + a/x ) / 2

def mysqrt(a):
	x = a/2
	epsilon = 0.000001
	while True:
		y = (x + a/x) / 2
		if abs(x-y) < epsilon:
			break
		x = y
	return x

def test_square_root(n):
	print("a" + ' '*4 +
		  "mysqrt(a)" + ' '*4 +
		  "math.sqrt" + ' '*4 +
		  "diff")
	print("-" + ' '*4 +
	  "---------" + ' '*4 +
	  "---------" + ' '*4 +
	  "----")	
	i = 1
	row = ""
	while i <= n:
		myresult = mysqrt(i)
		pythonresult = math.sqrt(i)
		row = str(i) + ' '
		row = row + str(myresult) + ' '*4 
		row = row + str(pythonresult) + ' '*4 
		row = row + str( (myresult - pythonresult) )
		print(row)
		i = i+1
		
test_square_root(10)