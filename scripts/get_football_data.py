import requests
import json

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'fdec4dd30f0d4bf9836514a25365a6c1' }


uri_competitions = "https://api.football-data.org/v4/competitions"

response = requests.get(uri_competitions, headers=headers)

for competition in response.json()['competitions']:
    if competition['name']=='Primera Division':
        la_liga_id = competition['id']
        break

uri_la_liga = f"https://api.football-data.org/v4/competitions/{la_liga_id}/matches"

response = requests.get(uri_la_liga, headers=headers)

first_match = list(response.json().keys())[0]

print(response.json().keys())
print(response.json()[first_match])
