#dictionary comprehensions create dictionaries using an expression and can replace for loops and certain lambda functions
#dictionary = {key_expression: value_expression for expression in iterable}

#a dictionary of temperature of cities in Fahrenheit, the city is the key and the temperature is the value
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#convert the temperature of each city to Celsius, conversion for each key/value pair is done in the cities in the dictionary above
cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

#using a if conditional statement
weather = {'New York': 'sunny', 'Boston': 'cloudy', 'Los Angeles': 'sunny', 'Chicago': 'rainy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

#using a conditional statement and an if/else statement
is_sun_out = {key: ("sun is out" if value == 'sunny' else "sun is not out") for (key, value) in weather.items()}
print(is_sun_out)