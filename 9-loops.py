numbers = [1, 12, 13, 4]

# Simple for loop	
for number in numbers:
	print(number)

print('\n' * 5) # Creates 5 new lines

# Looping through a range
for i in range(1, 10) :
	print(i)

# Sum all numbers in a list
print('\n')
numbers_list = [3, 4, 2, 1, 5]

sum = 0
for i in numbers_list :
	sum += i

print(sum)

# Iterate through a list
fruits = ['mango', 'apple', 'banana']

for fruit in fruits :
	print('\n' + fruit)

# list of dictionaries
persons = [{
	'name': 'abc',
	'age': 21
}, {
	'name': 'xyz',
	'age': 31
}]

personsLen = len(persons)

for i in range(personsLen):
	for key in persons[i]:
		print(persons[1][key])