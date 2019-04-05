from enum import Enum

class URLS(Enum):
    
    player_url = 'https://api.pubg.com/shards/{platform}/players?filter[{by}]={value}'
    seasons_url = 'https://api.pubg.com/shards/steam/seasons'
    player_season_url = 'https://api.pubg.com/shards/steam/players/{playerId}/seasons/{seasonId}'
    lifetime_url = 'https://api.pubg.com/shards/steam/players/{playerId}/seasons/lifetime'
    match_url = 'https://api.pubg.com/shards/steam/matches/{matchId}'
