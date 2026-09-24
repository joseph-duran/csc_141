'''
Joseph Duran
Chapter 3
This list shows evry function.
'''

Music_artist = ['Drake', 'Bruno Mars', 'Taylor Swift', 'Ariana Grande', 'Brent Faiyaz']
print(Music_artist)

message = [" = Goodmoring, Hello, How are you doing today? ", " = "
"Whats up! ", " = , How are you doing today? ", " = ", " How have you been?"]
print(Music_artist[0] +"," + message[0])

for guest in Music_artist:
    print("Hello and welcome to the party " + guest + "!")

print(Music_artist)
del Music_artist[4]
print(Music_artist)

Music_artist.append("J Cole")
for guest in Music_artist:
    print("Has been invited " + guest + "!")

    Music_artist.sort(reverse=True)
print(Music_artist)

print(len(Music_artist))
