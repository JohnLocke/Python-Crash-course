# City Names
def city_country(city, country):
    """Return a city and its country, neatly formatted."""
    full_string = f"{city}, {country}"
    return full_string


outcome = city_country('Beijing', 'China')
print(outcome)
outcome = city_country('Pairs', 'France')
print(outcome)
outcome = city_country('New York', 'the US')
print(outcome)
