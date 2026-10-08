'''Joseph Duran
Chapter 6
This program will show the names of some rivers and the countries they run through.
4/10'''

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'united states',
    'danube': 'germany'
}

for river, county in rivers.items():
    print(f"The {river.title()} river runs through {county.title()}.")