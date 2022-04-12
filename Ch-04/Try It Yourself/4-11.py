# My pizzaz, Your pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:



#    Make sure each new pizza is stored in the appropriate list.

# The original list with added topping
pizzas = ['pepperoni', 'jalepeno', 'sausage']
friend_pizzas = pizzas[:]

#   -Add a new pizza to the original list.

pizzas.append('pineapple')

#   -Add a different pizza to the list friend_pizzas
friend_pizzas.append('bacon')

#   -Prove that you have two separate lists. print the message My favorite pizzas are:, and then use a for loop to print the first list. 
print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

#    Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list.
print(f"My favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    