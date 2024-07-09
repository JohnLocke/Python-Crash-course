squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# clear the list
squares = []
print(squares)

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)
