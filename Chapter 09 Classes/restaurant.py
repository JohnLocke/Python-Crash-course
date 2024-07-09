"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints these two pieces of information: restaurant_name and cuisine_type."""
        print(f"{self.restaurant_name} is the name of the restaurant.")
        print(f"And it is famous for {self.cuisine_type}.\n")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open now!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers who’ve been served."""
        if number >= 0:
            self.number_served += number
        else:
            print("Impossible!")