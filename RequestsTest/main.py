import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '49a3498cb8b21377812a34bb43f69203'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "ryumshina.maria.a@yandex.ru", 
    "password": "Hokkaido11.04.2024"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Завр",
    "photo_id": 12
}
body_update = {
    "pokemon_id": "43218",
    "name": "Лис",
    "photo_id": 37
}

body_in_pokeboll = {
    "pokemon_id": "43349"
}


'''respons = requests.post(url = f'{URL}/trainers/reg',headers = HEADER, json = body_registration)
print(respons.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


#ДЗ

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''


'''response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)'''

'''message = response_update.json()['message']
print(message)'''

'''response_in_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeboll)
print(response_in_pokeboll.text)'''

'''message = response_in_pokeboll.json()['message']
print(message)'''



response_get_trainers = requests.get(url = f'{URL}/trainers', headers = HEADER)
print(response_get_trainers.status_code)
message = response_get_trainers.text
print(message)


response_get_trainers = requests.get(url = f'{URL}/trainers', headers = HEADER)
print(response_get_trainers.text)
message = response_get_trainers.json()['message']
print(message)