# The if_elif_statement is very powerful but is only appropiate when you want one test to pass.
# Sometimes it is important to check all the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks
#Let's reconsider the pizzeria example. If someone requests two-topping pizza, you'll need to be sure to include both toppintgs on their pizza:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


# This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes. Here's what that would look like:
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than  one block of code needs to run, use a series of independent if statements.