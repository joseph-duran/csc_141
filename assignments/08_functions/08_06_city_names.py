'''
Joseph Duran
Chapter 8
This program will show the names of cities.
4/10
'''
def city_name(city, country):
    """Return a string of the city and country."""
    return f"{city.title()} {country.title()}"

print(city_name("new york", "united states"))
print(city_name("Los angeles", "united states"))
print(city_name("paris", "france"))
print(city_name("tokyo", "japan"))
