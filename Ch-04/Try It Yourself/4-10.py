# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

animals = ['Cheetah', 'Tiger', 'Lion', 'Bobcat', 'Jaguar']
for animal in animals:
    print(f"A {animal.title()} will eat you.")
print(f"However people still keep them as pets.... smh.")

# Print the messages 'The first three items in the list are:.' Then use a slice to print the first three items from that program's list.
print(f"\nThe first three items in the list are:.")
for animal in animals[0:3]:
    print(animal.title())

# Print the message 'Three items from the middle of the list are:.' Use a slice to print three items from the middle of the list.
print(f"Three items from the middle of the list are:.")
for animal in animals[1:4]:
    print(animal.title())

# Print the message 'The last three items in the list are:.' Use a slice to print the last three items in the list.
print(f"The last three items in the list are:.")
for animal in animals[2:5]:
    print(animal.title())
