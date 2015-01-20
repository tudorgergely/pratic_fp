from domain.ValidationError import *

class WordValidator:
	def __init__(self):
		pass

	def validate_value(self, value):
		if len(value) < 2:
			raise ValidationError('Word value is too short. Give at least 2 chars')
		if not value.isalpha():
			raise ValidationError('Word can only contain letters')

	def validate_points(self, points):
		if points < 0:
			raise ValidationError('Word points have to be positive')