# Using the keywords 'and' and 'or' can help you check multiple conditions at the same time.

# Using 'and' to Check Multiple Conditions
# To check whether two conditions are true simultaneously, use the keyword and to combine the two conditionsl test;
# If both pass the overall expressions returns true.
# If one of them fails then the expression returns fals.
# For example, to check if two people are 21:
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 and age_1
# This will return 'False'

age_1 = 22
age_0 >= 21 and age_1 >= 21


# To improve readability, you can use parenteses around the individual teats, but they are not required. If you use parentheses, your test would look like this:
(age_0 >= 21) and ( age_1 >= 21)
