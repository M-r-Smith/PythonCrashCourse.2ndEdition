# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three dictioanaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

people = {
    'myself': {'first': 'marquiz',
            'last': 'smith',
            'city':'washington, d.c.',
            },
    'alvin':{'first': 'alvin',
            'last': 'chipmunk',
            'city': 'los angelas, california',
            },
    'alice':{'first': 'alice',
            'last': 'likkell',
            'city': 'london, england',
            },
}
for people_name, people_info in people.items():
    print(f"\nPersons name: {people_name}")
    full_name = f"{people_info['first']} {people_info['last']}"
    city = people_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tCity: {city.title()}")