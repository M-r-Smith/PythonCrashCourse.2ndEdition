# Working with Dictionaries
# A dictionary in python is a colectikon of key-value pairs. Each key is connected to a vlue, and you can use a 
# key to access the value associated with that key. A key's value can be a number, a string, a list, or even
# another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. 
# a key-pair is a set of values associated with each other. When you provide a key, python returns the value associated with that key.

# Accessing Values in a Dictionary
# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
alien_0 = {'color': 'green'}
print(alien_0['color'])

# You can have an unlimited number of key-value pairs in a dictionary. for example, here's the original alien_0 = {'color': 'green', 'points': 5}
# This is how you look up the point value of alien_0.
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

