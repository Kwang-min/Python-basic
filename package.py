#from animal import Dog
#from animal import cat
#from animal import *

#puppy = Dog()
#puppy.hi()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="min")
location = geolocator.geocode("seoul,south korea")

print(location.longitude)




