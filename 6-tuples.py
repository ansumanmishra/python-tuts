import sys
import os

tuple_1 = (1, 2, 3, 4, 5) # Can't the change the values once defined
print(tuple_1)

# Length of tuple
print(len(tuple_1))

# Max & Min
print(max(tuple_1))
print(min(tuple_1))

# Convert tuple to list
new_list = list(tuple_1)
print(new_list)

tuple_2 = tuple(new_list)
print(tuple_2)