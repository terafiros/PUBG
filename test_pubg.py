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

url = "https://api.pubg.com/shards/steam/matches/11e5041a-71a5-4612-9587-0ad22cf7b954"

player = pubg.get_player('Tecnosh')

#data, included, links, meta
'''
data
---'type'
---'id'
---'attributes'
---'relationships'
---'links'
'''



print(pubg.get_match(player.matches_ids[-1]).asset.id)

