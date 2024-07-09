# Ice Cream Stand
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints these two pieces of information: restaurant_name and cuisine_type."""
        print(f"{self.restaurant_name} is the name of the restaurant.")
        print(f"And it is famous for {self.cuisine_type}.\n")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open now!")


class IceCreamStand(Restaurant):
    """An ice cream stand is a specific kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize name, type and flavor attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Displays all these flavors."""
        for flavor in self.flavors:
            print(flavor)


new_stand = IceCreamStand("Sweet Shop", "Ice Cream", ["strawberry", "chocolate", "mango"])
new_stand.display_flavors()
