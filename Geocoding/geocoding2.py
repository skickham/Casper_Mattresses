#geocoding casper

#import pandas, the geocoder, and time
import pandas as pd 
from geopy.geocoders import Nominatim
import time

'''
things to change for each file:
n = the number of observations to run through
filepath = what the geocoded dataframe will be saved as
filenumber = starting with 0, which file this is, so it can affect the offset

*Note:*
offset will calculate itself based on what filenumber th euser is on 
'''

#variables to change
##################################################
n=1000
filepath = 'location_data/location2.csv'
filenumber = 2
offset = n * filenumber
##################################################



#start the timing
start = time.time()

#read in the location file as casper
casper = pd.read_csv('casper_with_location2.csv')

#init the geolocator
geolocator = Nominatim()

#init the location, latitude, and longitude lists
location_lst = []
lat_lst = []
long_lst = []

#run through the desired observations
for i in range(n):
    try:
        x = geolocator.geocode(casper.city_state[i + offset], timeout=100)
        location_lst.append(x.address)
        lat_lst.append(x.latitude)
        long_lst.append(x.longitude)
    except:
        location_lst.append('None')
        lat_lst.append('None')
        long_lst.append('None')


location = pd.DataFrame(
    {'city_state': casper.city_state[offset:n + offset],
     'location': location_lst,
     'latitude': lat_lst,
     'longitude': long_lst
    })

#print head in terminal
print(location.head())

#end the timer & print the time in terminal
end = time.time()
total_time = end - start
print('\n===============================================\nThis took {} seconds'.format(total_time))

#save file
location.to_csv(filepath)