# Conditional Tests
# An expression that can be evaluated as True or False is called a conditional test.
# Python uses the value true or false to decide whether the code in an if statement should be executed. 
# If the value is false, python ignores the code following the if statement.

# Checking for Equality
# The simplest conditional test checks whether the value of a variable is equal to the value of interest:
car = 'bmw'
car == 'bmw'
# Line 1 sets the value of car to 'bmw' using a single equal sign
# line 2 checks whether the value of car is 'bmw' using a double equal sign.
# The double equal sign is called an equality operator. It returns true if the values on the left and right side of the operator match, and false if the don't match

# Ignoring Case When Checking for Equality
# Testing for equality is case sensitive in python.
# However you can work around this by adding 'lower()' 
car = 'Audi'
car.lower() == 'audi'