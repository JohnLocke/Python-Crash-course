# Pets
pet_0 = {
    'type': 'dog',
    'owner': 'john',
}

pet_1 = {
    'type': 'cat',
    'owner': 'jason',
}

pet_2 = {
    'type': 'bird',
    'owner': 'jaylen',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type']}.")
