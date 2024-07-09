# Album
def make_album(artist_name, album_title, number_of_songs=None):
    """ Return a dictionary of information about a person. """
    if number_of_songs:
        album_info = {'name': artist_name, 'title': album_title, 'numbers': number_of_songs}
    else:
        album_info = {'name': artist_name, 'title': album_title}
    return album_info


album = make_album('Eminem', '8 Mile')
print(album)
album = make_album('Eminem', '8 Mile', 15)
print(album)
