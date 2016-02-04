import copy

class Kangaroo:
	
	def __init__(self, pouch_contents=[]):
		self.pouch_contents = copy.deepcopy(pouch_contents)
	
	def put_in_pouch(self, x):
		self.pouch_contents.append(x)
	
	#calling str directly inside here just recalled
	#str...and I had infinite recursion
	def __str__(self):
		s = ''
		for x in self.pouch_contents:
			s = s + object.__str__(x)
		return 'Kangaroo items: ' + s
		
kanga = Kangaroo()
roo = Kangaroo()
print(kanga.pouch_contents is roo.pouch_contents)
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
print(kanga.pouch_contents is roo.pouch_contents)