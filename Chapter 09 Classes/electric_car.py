# Storing Multiple Classes in a Module

"""A set of classes that can be used to represent electric cars."""

from car import Car


# Instances as Attributes
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        car_range = "unknown"
        if self.battery_size == 40:
            car_range = 150
        elif self.battery_size == 65:
            car_range = 225
        print(f"This car can go about {car_range} miles on a full charge.")


# Importing a Module into a Module
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    # The __init__() Method for a Child Class
    # Defining Attributes and Methods for the Child Class
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    # Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print(f"{self.make.title()} {self.model.title()} doesn't have a gas tank!")

