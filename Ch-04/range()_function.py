# Python's range() function makes it easy to generate a series of numbers. 
# This line of code will execute the number 1-4 because 0 is always the beginning.
for value in range(1, 5):
    print(value)

# To print the numbers from 1 to 5, you would use range(1, 6):
for value in range(1, 6):
    print(value)
    
    
# Using range() to Make a List of Numbers
# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.
# Wrapping list() around a call to the range() function will output a horizontal list.
numbers = list(range(1, 6))
print(numbers)


# We can also use range to tell python to skip numbers in a given range.
# If you add a third argument to range(), python uses that value as a step size whn generating numbers.
# For example, here's how to list the even numbers between 1 and 10.
# The range() function starts with 2 and adds 2 until it reaches or passes the value of 11.
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# In python ** represents exponents to square numbers.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# To write this code more concisely, omit the temporary variable square and append each new value directly to the list:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)


# List Comprehensions
# A list comprehension allows you to generate this same list in just one line of code.
squares = [value**2 for value in range(1,11)]
print(squares)