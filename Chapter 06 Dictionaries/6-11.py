# Cities
cities = {
    'Beijing': {
        'country': 'China',
        'population': 21_540_000,
        'fact': "the captial of China",
    },

    'Pairs': {
        'country': 'France',
        'population': 11_000_000,
        'fact': "the captial of France",
    },

    'New York': {
        'country': 'the USA',
        'population': 8_390_000,
        'fact': 'not the captial of the USA',
    },
}

for city, info in cities.items():
    print(f"\n{city}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")
