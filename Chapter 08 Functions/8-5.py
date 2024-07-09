# Cities
def describe_city(city, country='China'):
    """ Display the name of a city and its country. """
    print(f"{city.title()} is in {country.title()}.")


# Call the function for three different cities, at least one of which is not in the default country.
describe_city("Beijing")
describe_city("Shanghai")
describe_city("Pairs", "France")

