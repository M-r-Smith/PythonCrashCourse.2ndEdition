# The easiest wat to add a new element to a list is to append the item to the list.
# When you append an element it is added to the end of the list.
# Using the same list we had in the previous example, we'll add the new element 'ducati' to the end of the list:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# This line of code adds ducati to the end of the list, aka. append.
motorcycles.append('ducati')
print(motorcycles)

# You can also start with an empty list and then add items using a series of append() calls.
# Using an empty list, let's add the elements 'honda', 'yamaha', and 'suzuki' to the list:
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

print(motorcycles)

# This code inserts an element at the beginning of a list making its value 0.
