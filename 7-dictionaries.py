import sys
import os

# This is similar to objects in Javascript. Looks similar to JSON object
person = {
	"fname": "Ansuman",
	"lname": "Mishra",
	"location": "Bhubaneswar"
}

# Getting values
print(person['fname'])
# or
print(person.get('fname'))

# Length of dictionary
print(len(person))

# Changing the value
person["location"] = 'Hyd'
print(person)

# Adding a new prop
person["nationality"] = "Indian"
print(person)

# Delete a prop
del person['location']
print(person)

# Get all the keys
print(person.keys())

# Get all the values
print(person.values())