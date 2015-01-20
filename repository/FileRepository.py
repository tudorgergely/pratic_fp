from domain.Word import *
from repository.RepositoryError import *

class FileRepository:
	def __init__(self, file_name):
		self.__file_name = file_name

		self.__word_list     = []
		self.__score         = 0
		self.__highest_score = 0

	def read_data(self):
		try:
			with open(self.__file_name, 'r') as f:
				self.__highest_score = int(f.readline())

				for line in f:
					line = line.strip().split(', ')

					word_value  = line[0]
					word_points = int(line[1])

					word = Word(word_value, word_points)

					if word not in self.__word_list:
						self.__word_list.append(word)
		except Exception:
			raise RepositoryError('File may be corrupted or missing. Read how much I could.')

	def write_data(self):
		with open(self.__file_name, 'w') as f:
			f.write(str(self.__score) + '\n')

			for word in self.__word_list:
				f.write(str(word) + '\n')

	def add_word(self, word):
		for key, value in enumerate(self.__word_list):
			if value == word:
				self.__word_list[key] = word
				break
		else:
			self.__word_list.append(word)

		self.write_data()

	def add_points(self, points):
		self.__score += points

		self.write_data()

	def set_high_score(self, high_score):
		self.__highest_score = high_score

	def get_list(self):
		return self.__word_list

	def get_score(self):
		return self.__score

	def get_highest_score(self):
		return self.__highest_score
