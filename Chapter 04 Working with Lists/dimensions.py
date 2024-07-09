dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Python will raise an error when a line of code tries to alter a tuple.
# dimensions[0] = 250

# Tuples are technically defined by the presence of a comma.
my_t = (3,)
print(my_t)

for dimension in dimensions:
    print(dimension)

# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple.
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

print('\nModified dimensions:')
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)


