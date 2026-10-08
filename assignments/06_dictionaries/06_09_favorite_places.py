'''
Joseph Duran
Chapter 6
This program will display information about favorite places.
7/10
'''
favorite_places = []


place = {
    'name': 'Central Park',
    'city': 'New York',
    'country': 'USA'
}

favorite_places.append(place)

place = {
    'name': 'The Louvre',
    'city': 'Paris',
    'country': 'France'
}

favorite_places.append(place)

place = {
    'name': 'Machu Picchu',
    'city': 'Cusco',
    'country': 'Peru'
}

favorite_places.append(place)

for place in favorite_places:
    name = place['name']
    city = place['city']
    country = place['country']

    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Country: {country}")
    print()