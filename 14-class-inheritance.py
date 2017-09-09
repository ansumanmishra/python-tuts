class Parent:
	def __init__(self):
		print("Parent Constructor")

	def parent_method(self):
		return "From parent method"

	def welcome(self):
		return "Welcome parent"

	def __hidden_method(self):
		return "Hidden method"

class Child(Parent):
	def __init__(self):
		print("Child Constructor")

	def child_method(self):
		return "From child method"

	def welcome(self):
		return "Welcome child - Parent overriden"

c = Child()
print(c.child_method())
print(c.parent_method())
print(c.welcome())
print(c.__hidden_method()) # This will give exception as we can't access private methods/attributes from outside of the class