#You can use f-strings to compose complete message using the information associated with a variable, as shown here:

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#The title method changes the name to title case.