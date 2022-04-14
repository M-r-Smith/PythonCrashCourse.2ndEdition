# 5-6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
#   -If the person is less than 2 years old, print a message that the person is a baby.
#   -If the person is atleast 2 years old but less than 4. print a message that the person is a toddler.
#   -If the person is atleast 13 years old but less than 20, print a message thtat the person is a teenager.
#   -If the person is atleast 20 years old but less than 65, print a message that the person is an adult.
#   -If the person is age 65 or older, print a message that the person is an elder.
age = 45
if age < 2:
    person = 'baby'
    print("This person is a baby")
elif age < 4:
    person = 'toddler'
    print("This person is a toddler")
elif age < 20:
    person = 'teenager'
    print("This person is a teenager")
elif age < 65:
    person = 'adult'
    print("This person is an adult")
else:
    person = 'elder'
    print("This person is an elder")




    