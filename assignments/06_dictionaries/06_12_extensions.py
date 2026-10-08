'''
Joseph Duran
Chapter 6
This program will display
2/10
'''

person = {
    'first_name': 'Joseph',
    'last_name': 'Duran',
    'age': 18,
    'city': 'San Diego',
    'fact': 'I love to play video games.',
}

full_name = f"{person['first_name']} {person['last_name']}"

print(f"Full Name: {full_name}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print(f"Fact: {person['fact']}")
