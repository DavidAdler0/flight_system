import json

import requests

from get_data import get_targets


def weather_score(weather):
    if weather['condition'] == "Clear":
        return 1.0
    elif weather["condition"] == "Clouds":
        return 0.7
    elif weather["condition"] == "Rain":
        return 0.4
    elif weather["condition"] == "Stormy":
        return 0.2
    else:
        return 0

def get_targets_wether():
    target_citys = get_targets()
    url = 'https://api.openweathermap.org/data/2.5/forecast?'
    appid = 'c7ccca8bc2cd66c5bf1a893c767968e2'
    targets_wether =[]
    for target in target_citys:
        city = target['City'].lower()
        params = {'q': city, 'appid': appid}
        weather_response = requests.get(url, params=params).json()['list']
        for hour in weather_response:
            if hour["dt_txt"]  == "2024-09-13 00:00:00":
                target_dict = {'city': f'{city}'}
                target_dict['condition'] = hour['weather'][0]['main']
                target_dict['weather_score'] = weather_score(target_dict)
                target_dict['winds'] = hour['wind']['speed']
                target_dict['clouds'] = hour['clouds']['all']
                targets_wether.append(target_dict)
    with open('targets_weather.json', 'w') as file:
        json.dump(targets_wether, file)
# get_targets_wether()

def find_max_wind():
    max = 0
    with open('targets_weather.json', 'r') as file:
        content = json.load(file)
    for target in content:
        if target['winds'] > max:
            max = target['winds']
    return max
def generate_wether_final_score():
    with open('targets_weather.json', 'r') as file:
        content = json.load(file)
    with open('targets_weather.json', 'w') as new_file:
        for target in content:
            target['total_score'] = (333 * target['weather_score']) + (33 * target['clouds']) + (15.11 * target['winds'])
        json.dump(content, new_file)

generate_wether_final_score()