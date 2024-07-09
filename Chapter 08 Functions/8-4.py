# Large Shirts
def making_shirt(size='large', message='I love Python'):
    """ Display the size of the shirt and the message printed on it. """
    print(f"The size of the shirt is {size}.")
    print(f"The message printed on the shirt is '{message}'.\n")


# A large shirt with the default message
making_shirt()
# A medium shirt with the default message
making_shirt('medium')
# a shirt of any size with a different message.
making_shirt('small', 'I love C++')
