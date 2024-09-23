import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bb801a5493bc42f386e2ce000e2248b3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4913'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_id():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["id"] == TRAINER_ID