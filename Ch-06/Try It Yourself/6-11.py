# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in, its approximate population,
# and one fact about the city. The keys for each city's dictioary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'd.c.':{
        'country': 'u.s.a',
        'population': '692,683',
    },
    'new york': {
        'country': 'u.s.a',
        'population': '8,419,000'
    },
    'tokyo': {
        'country': 'japan',
        'population': '125,800,000',
    }
}
for city_name, city_info in cities.items():

    print(f"\nCity name: {city_name}")
    country = f"{city_info['country']}"
    population = city_info['population']

    print(f"\tWhat country: {country.title()}")
    print(f"\tpopulation: {population.title()}")
