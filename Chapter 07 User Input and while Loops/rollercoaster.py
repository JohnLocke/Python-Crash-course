# When you use the input() function, Python interprets everything the user enters as a string.
# The int() function converts a string representation of a number to a numerical representation,
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
