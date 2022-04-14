# 5-9. No Users: Add an if test to hello_ admin.py to make sure the list of users is not empty.
#   -If the list is empty, print the message we need to find some users!
#   -Remove all of the usernames from your list, and make sure the correct message is printed.
usernames = ['admin', 'kory', 'leon', 'bridget', 'sarah']
empty = 'no user'
for username in usernames:
    if 'admin' in username:
        print(f"Hello admin, would you like to see a status report?")
    elif 'kory' in username:
        print(f"Hello, kory!")
    elif 'leon' in username:
        print(f"Hello, leon!")
    elif 'bridget' in username:
        print(f"hello, bridget!")
    elif 'sarah' in username:
        print(f"hello, sarah!")
if empty not in usernames:
    print(f"{empty.title()}.")