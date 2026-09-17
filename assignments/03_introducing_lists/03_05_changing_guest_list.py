'''
Joseph Duran
Chapter 3
This program shows the how to remove a guest.
'''

guests = ["Michael Jackson", "Travis Scott", "kanye West"]

for guest in guests:
    print("Hello and welcome to the party " + guest + "!")

Cant_make_it_to_the_party = "kanye West"
guests.remove(Cant_make_it_to_the_party)
print("guests")

print(f"\n {Cant_make_it_to_the_party.title()} cant make it to the party.")

print (" Michael jackson and Travis Scott are still coming to the party.")