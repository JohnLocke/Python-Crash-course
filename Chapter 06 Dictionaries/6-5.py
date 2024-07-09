# Rivers
rivers = {
    'Yangtze River': 'China',
    'Seine River': 'France',
    'Mississippi River': "USA"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
print()
for river in rivers.keys():
    print(river)
print()
for country in rivers.values():
    print(country)
print()