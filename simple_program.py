#program that works in console


import pandas as pd
#reading the final combinations csv and setting random values for functions to work
combinations = pd.read_csv('D:\Coding\Projects\MSFS routes generator\combinations_final.csv')
print (combinations)
distance_min_func = 1
distance_max_func = 2
number_of_results_func = 3
departure_icao_func = "eham"
arrival_icao_func = "lppt"
#function for when neither departure nor arrival airport is entered
def distance_only(**distance_min_func, **distance_max_func, **number_of_results):
#checking whether minimum distance value is larger then maximum distance
  if distance_min_func >= distance_max_func:
    print ("max. distance value must be higer then min. distance")
    
  else:
    #finding suitable results in dataframe and ajusting number of results in case it is bigger then number of found results
    combinations_distance_only = combinations.loc[(combinations["distance"] >= distance_min_func) & (combinations["distance"] <= distance_max_func)]
    if number_of_results > len(combinations_distance_only):
       number_of_results = int(len(combinations_distance_only))
       tempdf = combinations_distance_only.sample(n = number_of_results)
    else: 
       tempdf = combinations_distance_only.sample(n = number_of_results)
    for i in range(number_of_results):
      #prints results
       print ("departure airport: " + str(tempdf.iloc[i]['icao1']) + ", arrival airport: " + str(tempdf.iloc[i]['icao2']) + ", distance: " + str(tempdf.iloc[i]['distance'])) 
#function for when departure airport is entered (same )
def departure_airport(distance_min_func, distance_max_func, number_of_results, departure_icao_func):
    if distance_min_func >= distance_max_func:
      print ("max. distance value must be higer then min. distance")
    
    else:
  
      combination_departure_icao = combinations.loc[(combinations["distance"] >= distance_min_func) & (combinations["distance"] <= distance_max_func)]
      combination_departure_icao2 = combination_departure_icao.loc[(combinations["icao1"] == departure_icao_func)]
      if number_of_results > len(combination_departure_icao2):
         number_of_results = int(len(combination_departure_icao2))
       
         tempdf2 = combination_departure_icao2.sample(n = number_of_results)
      else: 
         tempdf2 = combination_departure_icao2.sample(n = number_of_results)


      for i in range(number_of_results):
          print ("departure airport: " + str(tempdf2.iloc[i]['icao1']) + ", arrival airport: " + str(tempdf2.iloc[i]['icao2']) + ", distance: " + str(tempdf2.iloc[i]['distance'])) 

def arrival_airport(distance_min_func, distance_max_func, number_of_results, arrival_icao_func):
    if distance_min_func >= distance_max_func:
      print ("min. distance value must be higer then min. distance")
    
    else:
  
      combination_arrival_icao = combinations.loc[(combinations["distance"] >= distance_min_func) & (combinations["distance"] <= distance_max_func)]
      combination_arrival_icao2 = combination_arrival_icao.loc[(combinations["icao2"] == arrival_icao_func)]
      if number_of_results > len(combination_arrival_icao2):
        number_of_results = int(len(combination_arrival_icao2))
       
        tempdf_arr = combination_arrival_icao2.sample(n = number_of_results)
      else: 
        tempdf_arr = combination_arrival_icao2.sample(n = number_of_results)


      for i in range(number_of_results):
         print ("departure airport: " + str(tempdf_arr.iloc[i]['icao1']) + ", arrival airport: " + str(tempdf_arr.iloc[i]['icao2']) + ", distance: " + str(tempdf_arr.iloc[i]['distance'])) 







query_departure_yes_no = input("enter departure airport? (y/n): ")

if query_departure_yes_no == "y":

    departure_icao = str(input("Departure airport icao: ")).upper()
    distance_min = int(input("min. distance: "))
    distance_max = int(input("max. distance: "))
    number_of_results = int(input("number of results: "))
    
    departure_airport(distance_min, distance_max, number_of_results, departure_icao)
    
elif query_departure_yes_no == "n":
    query_arrival_yes_no = input("enter arrival airport? (y/n): ")
    if query_arrival_yes_no == "y":
        arrival_icao = input("arrival airport icao: ").upper()
        distance_min = int(input("min. distance: "))
        distance_max = int(input("max. distance: "))
        number_of_results = int(input("number of results: "))
        
        arrival_airport(distance_min, distance_max, number_of_results, arrival_icao)
    else:
      distance_min = int(input("min. distance: "))
      distance_max = int(input("max. distance: "))
      number_of_results = int(input("number of results: "))
    
      distance_only(distance_min, distance_max, number_of_results)
    


    
