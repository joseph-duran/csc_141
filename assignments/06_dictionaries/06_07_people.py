'''Joseph Duran
Chapter 6
This program will display information about people.
7/10
'''
people = []


person = {
    'first_name': 'Joseph',
    'last_name': 'Duran',
    'age': 18,
    'city': 'San Diego',
    }


people.append(person)

person = {
    'first_name': 'Brad',
    'last_name': 'Smith',
    'age': 20,
    'city': 'Los Angeles',}


people.append(person)

person = {
    'first_name': 'Hailee',
    'last_name': 'Jones',
    'age': 19,
    'city': 'Chicago',
}

people.append(person)

person = {
    'first_name': 'Mike',
    'last_name': 'Johnson',
    'age': 21,
    'city': 'New York',
    }

people.append(person)

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']

    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print()