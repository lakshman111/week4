# 1. Look at these websites first:
#
#    http://www.fly.faa.gov/flyfaa/usmap.jsp
#    http://services.faa.gov/docs/services/airport


# 2. Write code to report weather information at various airports.
#
#    I have provided a Python module in this folder named "faa"
#    that contains a function that you will find helpful.
#
#    Your goal is to write code that will display weather
#    information for each airport code in the list below.
#
#    Example output for an airport code:
#
#    ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
#
#    Good luck!

airport_codes = ['ORD', 'SFO', 'JFK']

# Your code goes here:

from faa import get_weather
# Or could have done...
# import faa
# for code in airport_codes:
#   data = faa.get_weather(code)

for airport in airport_codes:
  print(get_weather(airport)['name'] + ": The temperature is ", get_weather(airport)['weather']['temp'], "and the wind is", get_weather(airport)['weather']['wind'])
