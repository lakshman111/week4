import faa
data = faa.get_weather('ORD')

assert data['city'] == 'Chicago'
assert data['name'] == 'Chicago OHare International'
assert data['ICAO'] == 'KORD'
