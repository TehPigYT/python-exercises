def get_temperature(city):
    cities = {"London": 26, "New York": 28, "Paris": 32, "Berlin": 24, "Rome": 35}

    return cities.get(city, "Unknown")
