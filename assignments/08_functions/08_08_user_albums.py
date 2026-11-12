'''
Joseph Duran
Chapter 8
This program will show you how to create a function that describes an album.
4/10
'''
'''
Joseph Duran
Chapter 8
This program will show the names of albums.
8/10
'''
from turtle import title


def make_album(artist, title, tracks = None):
    """Return a dictionary of the artist and title."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album("Travis Scott", "Astroworld"))
print(make_album("Drake", "Views", 10))
print(make_album("Michael Jackson", "Thriller", 9))

while True:
    print("\nPlease enter the name an artist and album title.")
    print("Enter 'q' to quit.")
    artist = input("Artist: ")
    title = input("Album Title: ")
    if artist == 'q':
        break
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)
    


