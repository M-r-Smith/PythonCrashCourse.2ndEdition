# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts at once and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))