import faa

# Change the following code all you want:

def get_city_for(airport):
  return faa.get_weather(airport)['city']
  

def get_temperature_at(airport):
  return faa.get_weather(airport)['weather']['temp']
  

def get_wind_at(airport):
  return faa.get_weather(airport)['weather']['wind']


# Do not change the code below this line.

print("O'Hare Airport serves the city of", get_city_for('ORD'))
print("The temperature is:", get_temperature_at('ORD'))
print("The wind is:", get_wind_at('ORD'))
