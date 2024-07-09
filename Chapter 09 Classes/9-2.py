# Three Restaurants
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints these two pieces of information: restaurant_name and cuisine_type."""
        print(f"{self.restaurant_name} is the name of the restaurant.")
        print(f"And it is famous for {self.cuisine_type}.\n")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is open now!")


restaurant_1 = Restaurant("Taco Bell", "Tex-Mex cuisine")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Burger King", "American fast food")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Annie's", "Italian cuisine")
restaurant_3.describe_restaurant()
