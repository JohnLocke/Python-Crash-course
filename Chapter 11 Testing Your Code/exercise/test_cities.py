# 11-1 City, Country
from city_functions import city_country


def test_city_country():
    """Do string of the form City, Country, such as Santiago, Chile work?"""
    formatted_string = city_country('beijing', 'china')
    assert formatted_string == 'Beijing, China'


# 11-2 Population
def test_city_country_population():
    """Do string of the form City, Country, such as Santiago, Chile -- population 500000 work?"""
    formatted_string = city_country('beijing', 'china', 20_000_000)
    assert formatted_string == 'Beijing, China - population 20000000'
