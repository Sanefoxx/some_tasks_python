import math

class Shape(object):

	def __lt__(self, other):
		return self.area < other.area

class Square(Shape):

	def __init__(self, side):
		self.area = side * side

class Rectangle(Shape):
	
	def __init__(self, width, height):
		self.area = width * height
		
class Triangle(Shape):

	def __init__(self, base, height):
		self.area = height * base / 2

class Circle(Shape):

	def __init__(self, radius):
		self.area = radius * radius * math.pi

class CustomShape(Shape):

	def __init__(self, area):
		self.area = area
		