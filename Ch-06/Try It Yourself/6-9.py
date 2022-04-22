# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {
    'marquiz': {'fav':['japan','egypt',],
        },
    'gaje':{'fav': ['korea', 'netherlands',],
        },
    'mariah':{'fav':['paris', 'ghana',],
        },
}
for person_name, person_info in favorite_places.items():
    print(f"\nPets name: {person_name}")
    fav = (f"{person_info['fav']}")

    print(f"\tFavorite location: {fav.title()}")
