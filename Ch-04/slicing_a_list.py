# Slicing a list
# To make a slice, you specify the index of the firt and last elements you want to work with.
# The following example involves a list of players on a team:
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

# You can also generate any subset of a list. If you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[1:4])

# If you don't omit the first index in a slice python automatically starts your slice at the beginning of the list:
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[:4])

# The opposite end if you want your slice to include the end of a list. For example:
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[2:])

# You can also output any slice from the end of a list. For example:
players = ['charles', 'matina', 'michael', 'florence', 'eli']
print(players[-3:])