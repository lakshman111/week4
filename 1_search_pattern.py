# Divvy Bikes

import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

young_latitude = 41.793414
young_longitude = -87.600915

for station in stations:
  station_latitude = float(station['latitude'])
  station_longitude = float(station['longitude'])

  latitude_delta = math.fabs(station_latitude - young_latitude)
  longitude_delta = math.fabs(station_longitude - young_longitude)

  # ??




print("The nearest station is:", "(no idea)")
print("There are", "(no idea)", "bikes there right now!")
