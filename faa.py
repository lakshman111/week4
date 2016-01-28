import json
from urllib.request import urlopen

def get_weather(airport_code):
  url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result
