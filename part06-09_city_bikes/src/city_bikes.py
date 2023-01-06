import math

def get_station_data(filename: str):

#Bike station information in dict
    stations_info_dict = {}

    with open(filename) as bikestations:

        for line in bikestations:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            stations_info_dict[parts[3]] = (float(parts[0]), float(parts[1]))

    
    
    return stations_info_dict



def distance(stations: dict, station1: str, station2: str):


    station_one = stations[station1]
    station_two = stations[station2]

    station_one_x = float(station_one[0])
    station_one_y = float(station_one[1])

    station_two_x = float(station_two[0])
    station_two_y = float(station_two[1])

    x_km = float((station_one_x - station_two_x) * 55.26)
    y_km = float((station_one_y - station_two_y) * 111.2)
    distance_km = math.sqrt(x_km**2 + y_km**2)


    
    return float(distance_km)

    
def greatest_distance(stations: dict):

    
    for x in stations.items():
        print(x)

    

        


  

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
