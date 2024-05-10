import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'c01556d828df71a34e6ac0b683fadcb0'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo": "generate"
}

body_update = {
    "pokemon_id": "26543",
    "name": "The Wasp",
    "photo": "https://dolnikov.ru/pokemons/albums/014.png"
}

body_catch = {
    "pokemon_id": "26618"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message = response_create.json()['message']
print(message) 
