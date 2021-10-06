# -----------------------------------------------------------
#Example of Greedy_algorithm
#(C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


#Places where we want to be heard
needed_places = {"berlin", "Warszawa", "Gdansk", "wiocha", "kraków", "Tychy"}


#List of radio stations 
radio_stations = {}
radio_stations["nie_wiem_co_gadam"] = {"Berlin", "Warszawa", "Niedzica"}
radio_stations["piss_tube"] = {"Tychy", "Kobior"}
radio_stations["live_fm"] = {"Wiocha", "Tarnow", "Krakow", "Tychy"}
radio_stations["Mario_fm"] = {"Gdansk", "Warszawa", "Lubusk"}
radio_stations["esk"] = {"Berlin", "Wiocha", "Turkow"}


#implementation of greedy algorithm
best_stations = set([])
earlier_covered = set([])
best_choice = None
needed_places_before = set([])

while needed_places != set([]) and needed_places_before != needed_places:
    needed_places_before = needed_places.copy()
    for station, cities in radio_stations.items():
        covered = needed_places & cities
        if len(covered) > len(earlier_covered):
            best_choice = station

    best_stations |= {best_choice}
    needed_places -= radio_stations[best_choice]



print(best_stations)