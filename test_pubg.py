from pubg import PUBG
import requests


key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'

plat = 'steam'


pubg = PUBG(key, plat)

header = {
    'Authorization': 'Bearer ' + key,
    'Encoding':'gzip'
    }

header2 = {
    'Authorization': 'Bearer ' + key,
    'Accept': 'application/vnd.api+json'
    }

url = "https://api.pubg.com/shards/steam/players/{idd}/seasons/lifetime"

player = pubg.get_player('Tecnosh')
seasons = pubg.get_seasons()

#resp = requests.get(url.format(idd=player.idd), headers=header2)

resp = pubg.get_lifetime_stats(player.idd)
print(resp.gameModeStats.squad_fpp)


