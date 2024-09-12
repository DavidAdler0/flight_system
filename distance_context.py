import json
import math

import requests
from get_data import get_targets

def generate_targets_locations():
    target_citys = get_targets()
    geographical_points = {}
    url = 'https://api.openweathermap.org/geo/1.0/direct?'
    appid = 'c7ccca8bc2cd66c5bf1a893c767968e2'
    for target in target_citys:
        city = target['City'].lower()
        params = {'q': city, 'appid': appid}
        response = requests.get(url, params=params).json()
        geographical_points[city] = {'lat': response[0]['lat'], 'lon': response[0]['lon']}


    with open('location_points.json', 'w') as file:
        json.dump(geographical_points, file)


def generate_base_points():
    response = requests.get('https://api.openweathermap.org/geo/1.0/direct?q=israel&appid=c7ccca8bc2cd66c5bf1a893c767968e2').json()
    base_location = {'israeli_base':{'lat': response[0]['lat'], 'lon': response[0]['lon']}}
    with open('location_points.json', 'r') as file:
        content = json.load(file)
    with open('location_points.json', 'w') as file:
        content.update(base_location)
        json.dump(content, file)

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance
generate_targets_locations()
generate_base_points()
def generate_destanation():
    with open('location_points.json', 'r') as file:
        content = json.load(file)
        base_lat = content['israeli_base']['lat']
        base_lon = content['israeli_base']['lon']
        targets_destanation = {}
        for target_name, target_location in content.items():
            targets_destanation[target_name] = {'distance': haversine_distance(target_location['lat'], target_location['lon'], base_lat, base_lon)}

    with open('targets_distance.json', 'w') as file:
            json.dump(targets_destanation, file)


