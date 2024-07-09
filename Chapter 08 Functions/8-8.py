# User Albums
def make_album(artist_name, album_title, number_of_songs=None):
    """ Return a dictionary of information about a person. """
    if number_of_songs:
        album_info = {'name': artist_name, 'title': album_title, 'numbers': number_of_songs}
    else:
        album_info = {'name': artist_name, 'title': album_title}
    return album_info


while True:
    print("\nPlease tell me the album’s artist and title.")
    print("(enter 'q' at any time to quit)")

    artist = input("The album's artist is: ")
    if artist == 'q':
        break

    title = input("The album's title is: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
