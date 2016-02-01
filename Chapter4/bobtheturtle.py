import turtle
import math

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)
		
def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

def circle(t, r):
	circumference = 2 * math.pi * r
	polygon(t, circumference/100, 100)

def arc(t, r, arc):
	segments = int(arc/360 * 100)
	circumference = 2 * math.pi * r
	for i in range(segments):
		t.fd(circumference/100)
		t.lt(360/100)
		

bob = turtle.Turtle()

square(bob, 100)
polygon(bob, 50, 10)
circle(bob, 10)
arc(bob, 20, 180)

turtle.mainloop()