from domain.WordValidator import *
from random import *

class Word:
	def __init__(self, word_value, word_points):
		self.__validator = WordValidator()

		self.__validator.validate_value(word_value)
		self.__validator.validate_points(word_points)

		self.__value  = word_value
		self.__points = word_points

	def __str__(self):
		return '{}, {}'.format(self.__value, self.__points)

	def __repr__(self):
		return __str__(self)

	def __eq__(self, x):
		return self.__value == x

	def get_value(self):
		return self.__value

	def get_points(self):
		return self.__points

	def set_value(self, new_value):
		self.__validator.validate_value(new_value)

		self.__value = new_value

	def set_points(self, new_points):
		self.__validator.validate_points(new_points)

		self.__points = new_points

	def get_scrambled(self):
		return ''.join(sample(self.__value,len(self.__value)))
