# Polling: Use the code in favorite_languages.py (page 97)
#   -Make a list of people who should take a the favorite languages poll. Include some names that are already in the dictionary and some that are not.
#   -Loop throught the list of people who shoild take the poll. If they have already taken the poll, print a message thanking them for responding.
#   -If they have not yet taken the poll, print a message inviting them to to take the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'eric': 'c#',
    'chris': 'java',
}
new_poll = ['eric', 'chris']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}, thank you for taking our poll.")
    if name in new_poll:
        language = favorite_languages[name].title()
        print(f"\n\tHello {name.title()}, would you like to take our favorite_language poll?\n")


