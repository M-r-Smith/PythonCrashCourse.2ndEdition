# If you only want to show the values, you would use the values() method to return a list of values without any keys.
# For example, if we want a  list of the programming languages without the name of the person:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
# When you see braces but no key_value pairs, you're probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.
    