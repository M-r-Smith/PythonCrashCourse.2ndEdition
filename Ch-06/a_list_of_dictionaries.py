# Nesting is used to store multiple features inside of eachother.
# You can store a list iside a dictionary, a dictionary iside a list, or even a dictionary inside another dictionary.

# A list of Dictionaries
# Make a list fo aliens in which each alien is a dictionary of information about that alien. For example, the following code builds a list of three aliens:
#aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
    
    
# In the following we use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"total number of aliens: {len(aliens)}")


# When its time to change colors, we can use a for loop and an if statement to change the color of aliens. 
# For example, to change the first three aliens to yellow, medium-speed aliens worth 10 points each, we could do this:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")