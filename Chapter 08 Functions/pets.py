def describe_pet(animal_type, pet_name):
    """ Display information about a pet. """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Positional Arguments
describe_pet('hamster', 'harry')
# Multiple Function Calls
describe_pet('dog', 'willie')
# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')
# keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')


# Default Values
# Any parameter with a default value needs to be listed after all the parameters that don’t have default values.
# This allows Python to continue interpreting positional arguments correctly.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')

# Equivalent Function Calls
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
