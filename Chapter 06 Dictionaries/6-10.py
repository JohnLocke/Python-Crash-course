# Favourite Numbers
favorite_numbers = {
    'Tatum': [0, 24],
    'Brown': [1, 7],
    'Curry': [11, 30],
    'Harden': [1, 13],
    'Kobe': [8, 24],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number are:")
    for number in numbers:
        print(f"\t{number}")