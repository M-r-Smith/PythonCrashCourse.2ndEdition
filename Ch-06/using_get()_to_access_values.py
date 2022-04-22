# The get() method requires a key as a first argument. As a second optional argument, you can passs the value to be returned if the key doesn't exist:
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If there's a chance the key you're asking for might not exist, consider using the get() method instead of the square bracket nothion.