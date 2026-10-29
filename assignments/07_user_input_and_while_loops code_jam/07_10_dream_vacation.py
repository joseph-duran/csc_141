'''
Joseph Duran
Chapter 7
This program will ask users about their dream vacation.
7/10
'''
Dream_vacation = {}
while True:
    name = input("What is your name? (type 'quit' to exit) ")
    if name.lower() == 'quit':
        break
    vacation = input("If you could visit one place in the world, where would you go?")
    Dream_vacation[name] = vacation

print("\nDream Vacation Poll Results:")
for name, vactaion in Dream_vacation.items():
    print(f"{name} would like to visit {vacation}.")
