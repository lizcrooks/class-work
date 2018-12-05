def city_country(city, country, population=''):
    """Generate a city and country name together with its population."""
    location = city.title() + ", " + country.title() 
    if population:
        location += " Population - " + str(population)
    return location