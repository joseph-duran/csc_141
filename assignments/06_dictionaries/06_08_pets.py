'''
Joseph Duran
Chapter 6
This program will display information about pets.
7/10
'''
pets = []


pet = {
    'name': 'Buddy',
    'animal': 'dog',
    'owner': 'Alice',
    }

pets.append(pet)

pet = {
    'name': 'Whiskers',
    'animal': 'cat',
    'owner': 'Bob',
    }

pets.append(pet)

pet = {
    'name': 'Tweety',
    'animal': 'bird',
    'owner': 'Charlie',
    }

pets.append(pet)

for pet in pets:
    name = pet['name']
    animal = pet['animal']
    owner = pet['owner']

    print(f"Name: {name}")
    print(f"Animal: {animal}")
    print(f"Owner: {owner}")
    print()