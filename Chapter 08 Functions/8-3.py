# T-shirt
def making_shirt(size, message):
    """ Display the size of the shirt and the message printed on it. """
    print(f"The size of the shirt is {size}.")
    print(f"The message printed on the shirt is '{message}'.")


# positional arguments
making_shirt("medium", "I love Python")
# keyword arguments
making_shirt(size="medium", message="I love Python")

