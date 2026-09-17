'''
Joseph Duran
Chapter 3
This program shows the insert of more people.
'''

guests = ["Michael Jackson", "Travis Scott", "kanye West"]

for guest in guests:
    print("Has been invited " + guest + "!")

Cant_make_it_to_the_party = "kanye West"
guests.remove(Cant_make_it_to_the_party)
print("guests")

print(f"\n {Cant_make_it_to_the_party.title()} cant make it to the party.")

print (" Michael jackson and Travis Scott are still coming to the party.")

guest = ["Michael Jackson", "Travis Scott", "kanye West"]

guests.insert(0, "Kendrick Lamar")

guests.insert(2, "Drake")

guests.append("J Cole")

for guest in guests:
    print("Has been invited " + guest + "!")
