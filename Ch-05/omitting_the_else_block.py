# Python doesn't need to use an else block at the end of an if-elif chain. Sometimes an else block is useful: somethimes
# its clearer to use an additional elif statement that catches the specific conditions of interest:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

# The else block is a catchall statement.
# If you have a specific final condition consider useing the elif block and omith the else block.