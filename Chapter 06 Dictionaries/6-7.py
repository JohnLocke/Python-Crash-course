# People
john = {
    'first_name': 'John',
    'last_name': 'Locke',
    'age': 21,
    'city': 'Beijing',
}

jason = {
    'first_name': 'Jason',
    'last_name': 'Tatum',
    'age': 25,
    'city': 'Boston',
}

jaylen = {
    'first_name': 'Jaylen',
    'last_name': 'Brown',
    'age': 26,
    'city': 'LA',
}

people = [john, jason, jaylen]

for p in people:
    print(f"Name: {p['first_name'].title()} {p['last_name'].title()}")
    print(f"Age: {p['age']}")
    print(f"City: {p['city']}\n")
