# Divvy Bikes


# He pushed the completed file to github.  I went to grab a coffee cuz I was crashing.  Oops.



import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
# OH SNAP, you don't have to keep tying the name of the file if you
# store it as a variable
stations = result['stationBeanList']

young_latitude = 41.793414
young_longitude = -87.600915

for station in stations:
  station_latitude = float(station['latitude'])
  station_longitude = float(station['longitude'])
  # why the float? Oh, because it is coming back as a string?

  latitude_delta = math.fabs(station_latitude - young_latitude)
  longitude_delta = math.fabs(station_longitude - young_longitude)
  distance_to_this_station = math.hypot(latitude_delta, longitude_delta)

  print("The distance from Young to", station['stationName'], ": ", distance_to_this_station)

  # now what?



print()
print("The nearest station is:", "(no idea)")
print("There are", "(no idea)", "bikes there right now!")
