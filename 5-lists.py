import sys
import os

# Creating list
first_list = ['list1', 'list2', 'list3']
print(first_list)

# Appending to list
first_list.append('list4')
print(first_list)

# Adding a new item to a defined position
first_list.insert(0, 'list0')
print(first_list)

# Length of a list
print(len(first_list))

# Create second list
second_list = ['list5', 'list6', 'list7']

# Combining lists
print(first_list + second_list)

# Getting elements from lists
print(first_list[1]) # Prints list2

# Remove from list by name
first_list.remove('list3')
print(first_list)

# Reverse list
animals = ["dog", "cow", "horse", "cat"]
animals.reverse()
print(animals)

# Sort list
animals.sort()
print(animals)

# Delete list
del animals
#print(animals)

# Max & Min of a list
list_numbers = [1, 5, 6, 7, 2]
print(max(list_numbers))
print(min(list_numbers))