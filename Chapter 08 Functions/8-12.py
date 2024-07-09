# Sandwiches
def make_sandwiches(*fillings):
    """ Print a summary of the sand-wich that’s being ordered. """
    print("\nMaking a sandwiches with the following fillings:")
    for filling in fillings:
        print(f"- {filling}")


make_sandwiches('egg')
make_sandwiches('ham', 'beef')
make_sandwiches('cheese', 'bacon', 'tomato')
