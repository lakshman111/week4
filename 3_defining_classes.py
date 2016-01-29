# Classifying things
# Classes vs. instances, data attributes, and methods.

import faa;

class Airport:

  # people ususally use "self" by social convention
  def city(self):
    # whenever you call a function (on line 23), it always passes the object on the left of the dot
    # every method must accept at least one parameter
    data = faa.get_weather(self.code)
    return data['city']

  def temp(self):
    data = faa.get_weather(self.code)
    return data['weather']['temp']

  def wind(self):
    data = faa.get_weather(self.code)
    return data['weather']['wind']

# give me a new instance of an airport
my_airport = Airport()
your_airport = Airport()

# putting data into that instance
my_airport.code = 'ORD'
your_airport.code = 'SFO'





print("O'Hare Airport serves the city of", my_airport.city())
print("O'Hare Airport serves the city of", your_airport.city())
print("The temperature is:", my_airport.temp())
print("The wind is:", my_airport.wind())
