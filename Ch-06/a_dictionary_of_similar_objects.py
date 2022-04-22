# You can also use a dictinary to store one kind of information about many objects. For example, say you want to poll a number of people ans ask them what their favorite programming language is.
# A dictionary is useful for storing the results foa simple poll, like this:
# favorite _languages = 
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C'
#     'edward': 'ruby',
#     'phil': 'python',
#  }

# favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
