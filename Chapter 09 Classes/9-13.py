# Dice
from random import randint


class Dice:
    """A simple attempt to represent a dice"""

    def __init__(self, sides=6):
        """Initialize sides attribute."""
        self.sides = sides

    def roll_dice(self):
       """Prints a random number between 1 and the number of sides the dice has"""
       print(randint(1, self.sides))


d6 = Dice()
print("10 rolls of a 6-sided die:")
for times in range(10):
    d6.roll_dice()
print()

d10 = Dice(10)
print("10 rolls of a 10-sided die:")
for times in range(10):
    d10.roll_dice()
print()

d20 = Dice(20)
print("10 rolls of a 20-sided die:")
for times in range(10):
    d20.roll_dice()


