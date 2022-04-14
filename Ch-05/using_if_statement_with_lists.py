# You can watch for special values that need to be treated differently than other values in the list.
# You can manage changing conditions efficiently, such as the availability of certain items in a restaurant throughout a shift. You can also begin to prove that your code works as you
# expect it to in all possible situations

# Checking for Special Items
# Make a list of toppings the customer has requested and using a loop to announce each topping as it's added to the pizza:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!")


# What if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
else:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
