# Removing an item using the del statement.
# If You know the position of the item you want to remove from a list, you can use the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# This code uses del to remove the first item, 'honda', from the list of motorcycles:
del motorcycles[0]
print(motorcycles)

# You can remove an item from any position using the del statement.
# Here is how you can remove the second item, 'yamaha'.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# This line deletes 'yamaha' from position 1.
del motorcycles[1]
print(motorcycles)


# Removing an Item Using the pop() Method.
# The pop() method removes the last item in a list, but lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# Popping items from any Position in a List
# You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")


# Removing an item by Value
# If you know the item you want to remove, you can use the remove() method.
# Here we will remove the value ducati.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


# You can also use the remove() method to work with a value that's being removed from a list. Let's remove the value 'ducati' and print a reason for removing it from the list:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")