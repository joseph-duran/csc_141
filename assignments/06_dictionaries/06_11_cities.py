'''
Joseph Duran
Chapter 6
This program will display information about cities.
7/10
'''
cities = []


city = {
    'name': 'New York',
    'country': 'USA',
    'population': 8336572
}

cities.append(city)

city = {
    'name': 'Paris',
    'country': 'France',
    'population': 2161000
}

cities.append(city)

city = {
    'name': 'Tokyo',
    'country': 'Japan',
    'population': 13960000
}

cities.append(city)

for city in cities:
    name = city['name']
    country = city['country']
    population = city['population']

    print(f"Name: {name}")
    print(f"Country: {country}")
    print(f"Population: {population}")
    print()