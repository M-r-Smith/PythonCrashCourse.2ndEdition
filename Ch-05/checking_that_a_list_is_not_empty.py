# Lets check whether the list of requested toppings is empty before building the pizza.
# If the list is empty, we'll prompt the user and make sure they want a plain pizza.
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")