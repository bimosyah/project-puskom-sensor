import requests
from api import API_NOMER_HP

response = requests.get(API_NOMER_HP)
nomer_hp = response.json()
# print(nomer_hp)
