import faa
data = faa.get_weather('ORD')


# these are essentially checking that you wrote your program correctly.
assert data['city'] == 'Chicago'
assert data['name'] == 'Chicago OHare International'
assert data['ICAO'] == 'KORD'
