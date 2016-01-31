def right_justify(s):
	print( ' '*(70 - len(s)) + s)
	
right_justify('monty')

def do_twice(f, val):
	f(val)
	f(val)
	
def print_spam():
	print('spam')
	
def print_twice(val):
	print(val + ' ' + val)

def do_four(f, val):
	do_twice(f, val)
	do_twice(f, val)
	
def do_twice2(f):
	f()
	f()		
	
def do_four2(f):
	do_twice2(f)
	do_twice2(f)
	
do_twice(print_twice, 'spam')
do_four(print_twice, 'spam2')

def drawVertical():
	print("|" + " "*11 + "|" + " "*11 + "|")

def drawGrid():
	print("+ ", "- "*4, "+ ", "- "*4, "+")
	do_four2(drawVertical)
	print("+ ", "- "*4, "+ ", "- "*4, "+")
	do_four2(drawVertical)
	print("+ ", "- "*4, "+ ", "- "*4, "+")
	
drawGrid()
