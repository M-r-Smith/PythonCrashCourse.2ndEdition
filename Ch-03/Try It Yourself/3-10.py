# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once

animals = ['panda', 'monkey', 'dog']
print(animals)

# sorted()
print(sorted(animals))

# reverse()
animals.reverse()
print(animals.reverse())

#pop()
animals.pop()
print(animals)

#del
del animals[0]
print(animals)

# lens()
len(animals)
print(len(animals))
