# We use the if-elif-else chain to test more than two possibilities.
# How can we determine a person's admission rate into an amusement park.
# The following code tests for the age group of a person and then prints an admission price message:
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    

# Rather than printing the admission price within the if-elif-else block, it would be more consice to set just the price inside the if-elif-else chain and then have a simple 
# print() call that runs after the chain has been evaluated:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")