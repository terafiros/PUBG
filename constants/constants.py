from enum import Enum

class URLS(Enum):
    
    player_url = 'https://api.pubg.com/shards/{platform}/players?filter[{by}]={value}'
    seasons_url = 'https://api.pubg.com/shards/{platform}/seasons'
    
    
    player_season_url = 'https://api.pubg.com/shards/{platform}/players/{playerId}/seasons/{seasonId}'
    lifetime_url = 'https://api.pubg.com/shards/{platform}/players/{playerId}/seasons/lifetime'
    
    match_url = 'https://api.pubg.com/shards/{platform}/matches/{matchId}'
    sample_url = 'https://api.pubg.com/shards/{platform}/samples'
    
    leaderboard_url = 'https://api.pubg.com/shards/{platform}/leaderboards/{gameMode}?page[number]={pageNumber}'
    tournaments_url = 'https://api.pubg.com/tournaments/{id}'
    
    status_url = 'https://api.pubg.com/status'

class Events(Enum):
    pass