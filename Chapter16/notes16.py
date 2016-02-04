class Time:
	"""Represents the time of day.
	
	attributes: hour, minute, second
	"""
	
def print_time(t):
	print '%.2d : %.2d : %.2d' % (t.hour, t.minute, t.second)
	
def is_after(t1, t2):
	return (t1.hour, t1. minute, t1.second) > (t2.hour, t2.minute, t2.second)

def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time
	
def add_time(t1, t2):
	seconds = time_to_int(t1) + time_to_int(t2)
	return int_to_time(seconds)
	
def mul_time(t, n):
	new_time = int_to_time(time_to_int(t) * n)
	return new_time

def avg_pace(t, dist):
	return mul_time(t, 1/dist)