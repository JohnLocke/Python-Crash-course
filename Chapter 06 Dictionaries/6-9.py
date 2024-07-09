# Favourite Places
favorite_places = {
    'john': ['Beijing', 'Pairs', 'Toronto'],
    'jason': ['LA', 'New York'],
    'jaylen': ['Boston'],
}

for people, places in favorite_places.items():
    if len(favorite_places[people]) == 1:
        for place in places:
            print(f"\n{people.title()}'s favorite place is {place}.")
    else:
        print(f"\n{people.title()}'s favorite place are:")
        for place in places:
            print("\t" + place)
