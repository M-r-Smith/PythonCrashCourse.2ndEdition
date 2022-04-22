# The following dictionary would store one person's username, first name, and last name:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# If you want to see everything stored in this user's dictionary you could loop through the dictionary using a for loop:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
# You can choose any names you want for these two variables. It would work just as well if you use abbreviations like this:
# for k, v in user_0.items()

# Lets recreate the code from page 97 called favorite_languages.py
# You can loop through each name and language just as it was shown above.

# Favorite_language.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")