# Using 'or' allows you to check multiple conditions as well, but it passes when either or both of the indiviual tests pass.
# An or expression only fails when both individual tests fail.
# Let's look for only one person to be 21 this time.

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

age_0 = 18
age_0 >= 21 or age_1 >= 21