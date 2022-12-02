import random

class Animal:

	def __init__(self):
		self.name = self.generate_name()

	def generate_name(self):
		names = ["Me", "Myself", "I"]
		return random.choice(names)
