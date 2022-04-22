# The keys() method is useful when you don't need to work with all of the values in a dictionary. Let's loop through the favorite_languages dictionary and print the names of everyone who took the poll:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
# The line at 1 tells python to pull all the keys form the dictionary favorite_languages and assign them one at a time to the variable naem. The output shows the names of everyone who took the poll.
# However looping through the keys is actually defaut behavior.

# You can use the keys() method explicitly if  it amke your code easier to read, or you can omit it if you wish.
# Lets loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we'll display a message about their favorite language:
favorite_languages = {
   'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
# You can also use the keys() method to find out if a particular person was polled. This time, let's find out if Erin took the poll:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# The keys() method isn't just for looping: it actually returns a list of all the keys, and the line at 1 simply checks if 'erin' is in this list.
    