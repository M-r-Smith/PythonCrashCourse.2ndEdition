# 3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
#   -Start with your program from exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#   -Use pop() to remove guests from your list one at a time until only two names remain in your list.
#    Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner. 
#   -Print a message to each of the two people still on your list, letting them know they're still invited.
#   -Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# This is the program from exercise 3-6.
guest_list = ['naruto', 'sakura', 'sasuke']
guest_list.insert(0, 'Rock Lee')
guest_list.insert(2, 'Neji')
guest_list.append('Guy')
print(guest_list)

# These are the removed guest using the pop() method.
remove_guest = guest_list.pop()
print(f"Sorry {remove_guest.title()} I don't seem to have enough space to accomodate you for dinner.")

remove_guest = guest_list.pop()
print(f"Sorry {remove_guest.title()} I don't seem to have enough space to accomodate you for dinner.")

remove_guest = guest_list.pop()
print(f"Sorry {remove_guest.title()} I don't seem to have enough space to accomodate you for dinner.")

remove_guest = guest_list.pop()
print(f"Sorry {remove_guest.title()} I don't seem to have enough space to accomodate you for dinner.")

# These are the guest left that i have space for
print(f"Hey {guest_list[0].title()} im still having a dinner tonight if you still wanted to come?")
print(f"Hey {guest_list[1].title()} im still having a dinner tonight if you still wanted to come?")

# Using del to remove the last two names from your list.
del guest_list[1]
print(guest_list)

del guest_list[0]
print(guest_list)