from controller.ControllerError import *

class AdministerUi:
	def __init__(self, controller):
		self.__controller = controller

	def print_words(self):
		try:
			lis = self.__controller.get_sorted_list()

			for word in lis:
				print(str(word))
		except ControllerError as e:
			print(e)

	def read_command(self):
		try:
			command = input()
			command = command.strip().split(' ')

			if len(command) == 1:
				if command[0] == 'play':
					return False
				elif command[0] == 'exit':
					raise SystemExit

			if len(command) == 3 and command[0] == 'add':
				self.__controller.add_word(command[1], command[2])
				return True

			print('Invalid command')
			return True
		except ControllerError as e:
			print(e)

			return True

	def run_administer(self):
		try:
			self.__controller.read_data()
		except Exception as e:
			print(e)
		
		print('You are in administer mode')

		while True:
			self.print_words()
			
			result = self.read_command()

			if result == False:
				break

