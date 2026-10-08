'''
Joseph Duran
Chapter 6
This program will show you people's favorite numbers.
4/10
'''
favorite_numbers = {
    'Joseph': 7,
    'Joe': 3,
    'John': 5,
    'James': 9,
    'Hailee': 1,}

print(f"Joseph's favorite number is {favorite_numbers['Joseph']}.")
for key, value in favorite_numbers.items():
    print(f'The key is {key} and the value is {value}.')
