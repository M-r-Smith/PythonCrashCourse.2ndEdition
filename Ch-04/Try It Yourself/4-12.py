# 4-12. More Loops: all versions of foods.py in this section ahve avoided using for loops when printing to save space.
# Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(f"{my_food.title()}")

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(f"{friend_food.title()}")