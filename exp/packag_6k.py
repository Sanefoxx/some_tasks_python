class DimensionsOutOfBoundError(Exception):
	def __init__(self, prop, value, low, up):
		Exception.__init__(self, "Package {0}=={1} out of bounds, should be: {2} < {0} <= {3}".format(prop, value, low, up)	) 


class Package(object):

	def __init__(self, length, width, height, weight):
		
		if length > 350 or length <= 0:
			raise DimensionsOutOfBoundError("length", length, 0, 350)
		self.length = length

		if width > 300 or width <= 0:
			raise DimensionsOutOfBoundError("width", width, 0, 300)
		self.width = width

		if height > 150 or height <= 0:
			raise DimensionsOutOfBoundError("height", height, 0, 150)
		self.height = height

		if weight > 40 or weight <= 0:
			raise DimensionsOutOfBoundError("weight", weight, 0, 40)
		self.weight = weight
		
		self.volume = self.__length * self.__width * self.__height

	@property
	def volume(self):
		return self.__length * self.__width * self.__height

	@volume.setter
	def volume(self, volume):
		self.__volume = volume

	@property
	def length(self):
		return self.__length

	@length.setter
	def length(self, length):
		if length > 350 or length <= 0:
			raise DimensionsOutOfBoundError("length", length, 0, 350)
		self.__length = length

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		if width > 300 or width <= 0:
			raise DimensionsOutOfBoundError("width", width, 0, 300)
		self.__width = width

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		if height > 150 or height <= 0:
			raise DimensionsOutOfBoundError("height", height, 0, 150)
		self.__height = height

	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, weight):
		if weight > 40 or weight <= 0:
			raise DimensionsOutOfBoundError("weight", weight, 0, 40)
		self.__weight = weight