# Python's if statement allows you to examine the current state of program and respond appropriately to that state.

# A Simple Example
# The value 'bmw' should be printed in all uppercase. The following code loops through a list of car names and looks for the value 'bmw'.
# Whenever the value is 'bmw', it's printed in uppercase instead of title case:

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())