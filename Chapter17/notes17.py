class Point:
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __str__(self):
		return '(%d, %d)' % (self.x, self.y)
		
	def __add__(self, other):
		if isinstance(other, Point):
			return add_point(other)
		else:
			return add_tuple(other)
	
	def __radd__(self,other):
		return self.__add__(other)

	def add_point(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def add_tuple(self, other):
		return Point(self.x + other[0], self.y + other[1])

class Time:

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
		
	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
	
	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)
			
	def __radd__(self, other):
		return self.__add__(other)
	
	def print_time(self):
		print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
		
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds
		
	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)
	
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)	
	
	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()
		
		
start = Time(9, 45)

start.print_time()

print(start)

#hasattr to check for attributes of an object
#vars(obj) also gives a dictionary of attributes