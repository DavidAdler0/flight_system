import requests

url = "https://api.openweathermap.org/geo/1.0/direct"
appid = 'c7ccca8bc2cd66c5bf1a893c767968e2'
city = 'teheran'
params = {'q': city, 'appid': appid}
response = requests.get(url, params=params)
print(response.json())