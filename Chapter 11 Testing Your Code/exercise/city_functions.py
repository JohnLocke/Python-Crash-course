# 11-1 City, Country
# def city_country(city, country):
#     """Return a single string of the form City, Country"""
#     city_country_string = f"{city}, {country}"
#     return city_country_string.title()


# 11-2 Population
def city_country(city, country, population=''):
    """Return a single string of the form City, Country and Population"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"






