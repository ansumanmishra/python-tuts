class Person:
	__fname = ""
	__lname = ""

	def __init__(self, fname, lname): # Constructor
		self.__fname = fname
		self.__lname = lname

	def set_fname(self, name): # Setter
		self.__fname = fname

	def get_fname(self): # Getter
		return self.__fname

	def set_lname(self, lname):
		self.__lname = lname

	def get_lname(self):
		return self.__lname

	def welcome_user(self):
		return 'hey ' + self.__fname + ' ' + self.__lname

person1 = Person('Ansuman', 'Mishra') # Initialize an instance of a class

print(person1.get_fname()) # Calling the getter method of a class
print(person1.welcome_user()) # Calling a method of a class

person2 = Person('abc', 'xyz')
print(person2.welcome_user())