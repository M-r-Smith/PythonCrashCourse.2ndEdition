# 6-10. Favorite Numbers: Modify your program from exercise 6-2 (page 99) so each person can have more than one favorite number.
# Then print each person's name along with their favorite numbers.
# Modified version of 6-2.
favorite_numbers = {'donte': [82, 92],
                    'christopher': [73, 49],
                    'dave': [65, 59],
                    'kristina': [21, 71],
                    'jaques': [44, 63]
                    }
favorite_number = favorite_numbers['donte']
print(f"Donte's favorite number is {favorite_number}")
favorite_number = favorite_numbers['christopher']
print(f"christopher's favorite number is {favorite_number}")
favorite_number = favorite_numbers['dave']
print(f"Dave's favorite number is {favorite_number}")
favorite_number = favorite_numbers['kristina']
print(f"kristina's favorite number is {favorite_number}")
favorite_number = favorite_numbers['jaques']
print(f"jaques's favorite number is {favorite_number}")