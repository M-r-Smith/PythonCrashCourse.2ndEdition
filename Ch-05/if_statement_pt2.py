# Lets dig deeper into if statements.

# Simple if statements
# The simplest kink of if statement has one test and one action:
# if conditional_test:
#   do something

# The following code tests whether the person can vote:
age = 19
if age >= 18:
    print("You are old enough to vote!")
    
# Indentation works the same way for if statements as the do in for loops.
# Lets write another line of output to see if the person is old enough to vote.
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
 