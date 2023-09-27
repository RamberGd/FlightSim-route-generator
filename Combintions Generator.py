import numpy as np
import pandas as pd
import random as rnd
import math
import itertools
import geopy as geo
import geopy.distance
from more_itertools import distinct_combinations

#reads csv with all airports info and adds to dataframe
df = pd.read_csv('D:\Coding\Projects\MSFS routes generator\Queries\query.csv')
df = df.rename(columns={'ICAO_airport_code': 'ICAO', 'itemLabel' : 'Name', 'countryLabel' : 'Country', 
                        'located_in_the_administrative_territorial_entityLabel' : 'Province', 
                        'coordinate_location' : "Coordinates" })
df['Coordinates'].str.split(' ')

#separates longtitude and latitude
df[['Longtitude', 'Latitude', ]] = df['Coordinates'].str.split(' ', expand=True)
del df['Coordinates']

#deletes unnecessary symbols 
df["Latitude"]= df["Latitude"].str.replace("Point",  " ",)
df["Latitude"]= df["Latitude"].str.replace(")",  " ",)
df["Longtitude"]= df["Longtitude"].str.replace("Point",  " ",)
df["Longtitude"]= df["Longtitude"].str.replace("(",  " ",)



#function for calculating distance between two points. it takes longtitude and latitude of each of two point as input  
def distance (lon1, lat1, lon2, lat2):
    #combines two longtitude and latitude into one string
    coords1 = str(lat1) + ' ' + str(lon1)
    
    coords2 = str(lat2) + ' ' + str(lon2)
    #gets distance between two sets of coordinates using geopy
    distanceresult = (geopy.distance.geodesic(coords1, coords2).nm)
    return distanceresult


       
dfcoords = df[['ICAO', 'Longtitude', 'Latitude']]
#makes dataframe a list
icaocoords = dfcoords.values.tolist()

#doesnt work without it 
icaocoords = [ list(map(str,x)) for x in icaocoords ]
combinations = sorted(distinct_combinations((icaocoords), 2))

#adds commas between objects in list
combinationsdf = pd.DataFrame(combinations, columns = ["Airport1", 'Airport2'])
combinationsdf['Airportzz'] = combinationsdf['Airport1'].apply(lambda x: ','.join(map(str, x)))
combinationsdf['Airportzz2'] = combinationsdf['Airport2'].apply(lambda x: ','.join(map(str, x)))

combinationsdf[['icao1', 'lon1', 'lat1']] = combinationsdf['Airportzz'].str.split(',', expand=True)

combinationsdf[['icao2', 'lon2', 'lat2']] = combinationsdf['Airportzz2'].str.split(',', expand=True)

combinationsdf.drop(['Airport1', 'Airport2', 'Airportzz', 'Airportzz2'], axis=1, inplace=True)


#lon and lat are swapped
combinationsdf['distance'] = combinationsdf.apply(lambda x: distance(x['lon1'], x['lat1'], x['lon2'], x['lat2']), axis=1)

print (combinationsdf)
#filters unnecessary columns and saves to csv
combinations_final = combinationsdf.filter(items=['icao1', 'icao2', 'distance'])
combinations_final.to_csv("combinations_final.csv")
print ("done")








    
 




 