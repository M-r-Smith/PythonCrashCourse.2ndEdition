# 3-8. Seeing the World: Think of at least five places in the world you'd like to visit


#   -Store the locations in a list. Make sure the list is not in alphabetical order.
travel_location = ['japan', 'egypt', 'italy', 'korea', 'netherlands']

#   -Print your list in its original order. Don't worry about printing the list neatly, just print it as a raw Python list.
print(travel_location)

#   -Use sorted() to print your list in alphabetical order without modifying the actual list.
#   -Show that your list is still in its original order by printing it.
print(sorted(travel_location))

#   -Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#   -Show that your list is still in its original order by printing it agin. 
travel_location.reverse()
print(travel_location)

#   -Use reverse() to change the order of your list. Print the list to show that its order has changed.
travel_location.reverse()
print(travel_location)

#   -Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
travel_location.reverse()
print(travel_location)

#   -Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
travel_location.sort()
print(travel_location)