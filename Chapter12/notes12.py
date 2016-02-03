a = 1
b = 2

#old way of switching variables
temp = a
a = b
b = temp

#the python way
a, b = b, a

#getting multiple return values from a function
quot, rem = divmod(7, 3)

#*gathers args or scatters

#gathering
def printall(*args):
	print(args)
	
t = (7,3)
#scattering
divmod(*t)

def sumall(*args):
	return sum(args)

print(sum( (1,2,3) ))
print(sumall(1,2,3))

s = 'abc'
t = [0, 1, 2]
zip(s, t)
#zip creates an iterator
for pair in zip(s, t):
	print(pair)

#get a list of the zipped
list(zip(s, t))

#use tuple assignment in a loop
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
	print(number, letter)
	
def has_match(t1, t2):
	for x, y in zip(t1, t2):
		if x == y:
			return True
	return False

for index, element in enumerate('abc'):
	print(index, element)
#prints
#0 a
#1 b
#2 c