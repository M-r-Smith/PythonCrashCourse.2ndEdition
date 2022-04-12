# Often you want to copy a list and make it into a new one.
# To copy a list you make a slice that includes the entire original list by ommiting the first and second index.([:])
# This tells python to make a slice that starts with the first item and ends with the last item, making a copy of the entire list.
# If a friend likes everything in our list so far, we would create their list by copying ours:
my_foods = ['pizza', 'falafel', 'carrot cake',]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends's favorite foods are:")
print(friend_foods)


# We will add new food to each list and show that each list keeps track of the appropriate person's favorite foods:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# If we had simply set friend_foods equal to my_foods, we wouldn't have to produce two separate lists. For, example, here's what happens when you try to copy a list without using a slice:
my_foods = ['pizza', 'falafel', 'carrot cake']

#   -this doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
