# You can add new key-value pairs to a dictionary at any time.
# Lets add two peices of information to the alien_0 dictionsry: the alien's x-and y- coordinates, which will help us display tyhe alien in a particular position
# on the screen. Let's place the alien on the left edge of the screen. 25 pixels down from the top. Because screen coodinates usually start at the upper-left
# corner of the screen, we'll place the alien on the left edge of the screen by setting the x-coordinate to 0 and 25 pixels from the top by setting its y-coordinate to positive 25, as shown here:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)