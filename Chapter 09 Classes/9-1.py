# Restaurant
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


restaurant = Restaurant("Panda Express", "American Chinese cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()



