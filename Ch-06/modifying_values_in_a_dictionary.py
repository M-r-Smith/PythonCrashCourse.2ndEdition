# Modifying Values in a Dictionary
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
# For example, consieder an alien that changes from green to yellow as a game progresses:

#alien.py
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# We first define a dictionary for alien_0 that contains only the alien's color: then we change the value associated with the key 'color' to 'yellow'.
# The output shows that the alien has indeed changed form green to yellow:


# For a more intersting example, let's track the position of an alien that can move at different speeds.
# We'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:
alien_0 = {'x_position': 0, 'y-position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")