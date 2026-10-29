'''Joseph Duran
Chapter 7
This program will ask the user for movie tickets and then display a message about the tickets.
6/10
'''
active = True
while active:
    age_of_person = input("What is your age?: ")
    if age_of_person == "quit":
        break
    elif int (age_of_person) < 3:
        print("Your ticket is free!")
    elif int (age_of_person) <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")