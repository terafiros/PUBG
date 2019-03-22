from pubg import PUBG
import requests


key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'

plat = 'steam'


p = PUBG(key, plat)

#3 dados, meta, links e data. meta -> vazio, links -> com o link da consulta e data -> o que interessa





header = {
    'Authorization': 'Bearer ' + key,
    'Encoding':'gzip'
    }

header2 = {
    'Authorization': 'Bearer ' + key,
    'Accept': 'application/vnd.api+json'
    }

url = "https://api.pubg.com/shards/steam/seasons"

response = requests.get(url, headers=header2)
print(response.text)
