# You can use a slice in a for loop if you want to loop through a subset of the elements in a list. In the next example we loop through 
# the frist three players and print their names as part of a simple roster:
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print("here are the first three players on my team:")
for player in players[:3]:
    print(player.title())