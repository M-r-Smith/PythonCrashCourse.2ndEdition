# Tuples are a list of items that cannot change.

# Defining a Tuple
# Tuples use parentheses instead of square brackets.
# For example, if we have a rectange that should always be a certain size, we can ensure that its size doesn't change by putting the dimensions into a tuple:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#   -Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:
#       -my_t = (3,)
#   -It doesn't make sense to build a tuple with one element, but this can happen when tuples are generated automatically.


# Looping Through All Values in a Tuple
# You can loop over all the values in a tuple using a for loop, just as you did with a list:
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    

# Writing over a Tuple
# You can assign a new value to a variable that represents a tuple. 
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)