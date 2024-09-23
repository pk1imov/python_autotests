import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bb801a5493bc42f386e2ce000e2248b3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Страдивариус",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Клювокрыл",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_add = {
    "pokemon_id": pokemon_id
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)