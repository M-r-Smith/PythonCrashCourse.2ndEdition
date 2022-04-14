# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user:
#   -If the username is 'admin', print a special greeting, such as Hello admin, yould you like to see a status report?
#   -Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
usernames = ['admin', 'kory', 'leon', 'bridget', 'sarah']
for username in usernames:
    if 'admin' == username:
        print(f"Hello admin, would yo like to see a status report?")
    elif 'kory' == username:
        print(f"Hello user, kory!")
    elif 'leon' == username:
        print(f"Hello user, leon!")
    elif 'bridget' == username:
        print(f"hello user, bridget!")
    elif 'sarah' == username:
        print(f"hello user, sarah!")
        