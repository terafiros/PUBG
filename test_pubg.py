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

url = "https://api.pubg.com/shards/steam/players/{playerId}/seasons/{seasonId}"

player = pubg.get_player('terafiros')
season = pubg.get_seasons()[-1]

stats = pubg.get_player_stats_for_season(player.idd, season.idd)

stats.gameModeStats.squad_fpp
