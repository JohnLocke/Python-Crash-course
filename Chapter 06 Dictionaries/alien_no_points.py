# Using get() to Access Values

# When you ask for the point value of an alien that doesn't have a point value set,
# it results in a traceback, showing a KeyError.
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# The get() method requires a key as a first argument. As a second
# optional argument, you can pass the value to be returned if the key doesn’t exist.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
