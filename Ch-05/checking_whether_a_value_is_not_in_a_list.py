# You can use the keyword 'not' to check if a value doesn't appear in a list.
# For example you can check to see if who is banned from commenting in aa forum. 
# You can check whether a user has been banned before allowing that person to submit a comment:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
