'''
Joseph Duran
Chapter 8
This program will show the names of albums.
4/10
'''
def make_album(artist, title, tracks = None):
    """Return a dictionary of the artist and title."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album("Travis Scott", "Astroworld"))
print(make_album("Drake", "Views", 10))
print(make_album("Michael Jackson", "Thriller", 9))
