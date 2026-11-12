""" Joseph Duran
Chapter 8
This program will show you how to describe cities.
4/10
"""
def describe_city(city, country = 'USA'):
    print(f'{city} is in {country}. ')

    describe_city('New York')
    describe_city('Los Angeles')
    describe_city("Paris", country = 'France')

