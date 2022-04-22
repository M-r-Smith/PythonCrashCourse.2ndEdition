# You can use the sorted() function to get a copy of the keys in order:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# Sorted() function is wrapped around the dictionary.keys() to sort the keys in alphabetical order.