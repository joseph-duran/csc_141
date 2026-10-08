'''
Joseph Duran
Chapter 6
This program will display information about favorite numbers.
5/10
'''
favorite_numbers = {}


favorite_numbers['Alice'] = [7, 13, 21]
favorite_numbers['Bob'] = [3, 9, 15]
favorite_numbers['Charlie'] = [5, 11, 17]

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}")