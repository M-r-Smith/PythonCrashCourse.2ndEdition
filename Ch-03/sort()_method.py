# Sorting a List Permanently with the sort() Method.

# The sort() method changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort this list in reverse alphabeticalby passing the argument 'reverse=True' to the sort() 
# method. The following example sorts the list of cars in reverse alphabetical order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a list Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order, you can use the 'sorted() Function
# to display your list in a particular order but won't affect the actual order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
