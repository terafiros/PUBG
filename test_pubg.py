from pubg import PUBG
import requests
from PIL import Image, ImageDraw

from telemetry import Telemetry
import json

def sem_api():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    header = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/vnd.api+json'
    }
    # url = "https://api.pubg.com/shards/steam/matches/11e5041a-71a5-4612-9587-0ad22cf7b954" 2019-03-09T03:05:38Z
    url = 'https://api.pubg.com/shards/steam/samples'  # ?filter[createdAt-start]=2019-03-23T10:49:00Z'
    rsp = requests.get(url, headers=header)
    m_id = 'e54ce173-3fe1-4059-982c-f260d737b177'

    player = pubg.get_player('terafiros')
    match = pubg.get_match(player.matches_ids[0])

    print(match.mapName)
    print(match.duration)
    print(match.gameMode)

    # 4326
    erangel = Image.open('maps/nova.png')
    miramar = Image.open('maps/miramar.jpg')

    print(miramar.mode)

    kill = Image.open('maps/Death.png')
    position = Image.open('maps/position.png')

    telemetry = requests.get(match.asset.URL)
    print(match.asset.URL)

    t = Telemetry(telemetry.json())

    count = 0
    verify = 0

    for ox, oy in t.player_kill():
        miramar.paste(kill, (int(ox), int(oy)), kill)

    for ox, oy, r in t.safety_zone_position():
        draw = ImageDraw.Draw(miramar)
        draw.ellipse((ox - r, oy - r, ox + r, oy + r), outline='green')

    '''
        if tele['_T'] == 'LogPlayerPosition':
            if tele['character']['name'] == 'Tecnosh':
                x = tele['character']['location']['x']
                y = tele['character']['location']['y']

                ox = 2048 * x / 816000
                oy = 2048 * y / 816000
                print(ox, oy)
                erangel.paste(position, (int(ox), int(oy)), position)
    '''

    miramar.show()

def com_api():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    
    #player_request(pubg)
    #player_json(pubg)
    
    #seasons_request(pubg)
    #seasons_json(pubg)
    
    #player_season_stats_request(pubg)
    #player_season_stats_json(pubg)
    
    #lifetime_request(pubg)
    #lifetime_json(pubg)
    
    #match_request(pubg)
    match_json(pubg)

def player_json(pubg):
    with open('terafiros.json') as data:
        player = pubg.get_player_from_json(json.load(data))
        print(player.name)
        print(player.type)
        print(player.id)
        print(player.updatedAt)
        print(player.titleId)
        print(player.shardId)
        print(player.createdAt)
        print( player.matches)
        print(player.name_search_url)
        print(player.id_search_url)

def player_request(pubg):
    player = pubg.get_player('terafiros')
    print(player.name)
    print(player.type)
    print(player.id)
    print(player.updatedAt)
    print(player.titleId)
    print(player.shardId)
    print(player.createdAt)
    print( player.matches)
    print(player.name_search_url)
    print(player.id_search_url)
    
def seasons_request(pubg):
    seasons = pubg.get_seasons()
    print(len(seasons))
    for season in seasons:
        print(season.id)
        print(season.type)
        print(season.isCurrentSeason)
        print(season.isOffseason)

def seasons_json(pubg):
    with open('seasons.json') as data:
        seasons = pubg.get_seasons_from_json(json.load(data))
        print(len(seasons))
        for season in seasons:
            print(season.id)
            print(season.type)
            print(season.isCurrentSeason)
            print(season.isOffseason)

def player_season_stats_request(pubg):
    season_id = ''
    player_id = ''
    
    with open('seasons.json') as data:
        seasons = pubg.get_seasons_from_json(json.load(data))
        season_id = seasons[-1].id
        
    with open('terafiros.json') as data:
        player_id = pubg.get_player_from_json(json.load(data)).id
    
    player_season_stats = pubg.get_player_stats_for_season(player_id, season_id)
    for elem in player_season_stats.gameModeStats.squad_fpp:
        print(elem, ':', player_season_stats.gameModeStats.squad_fpp[elem])
    

def player_season_stats_json(pubg):
    season_id = ''
    player_id = ''
    with open('seasons.json') as data:
        seasons = pubg.get_seasons_from_json(json.load(data))
        season_id = seasons[-1].id
        
    with open('terafiros.json') as data:
        player_id = pubg.get_player_from_json(json.load(data)).id
        
    with open(player_id + "_" + season_id + ".json") as data:
        player_season_stats = pubg.get_player_stats_for_season_from_json(json.load(data))
        for elem in player_season_stats.gameModeStats.squad_fpp:
            print(elem, ':', player_season_stats.gameModeStats.squad_fpp[elem])
        
    
def lifetime_request(pubg):
    player_id = ''
    with open('terafiros.json') as data:
        player_id = pubg.get_player_from_json(json.load(data)).id
    lifetime = pubg.get_lifetime_stats(player_id)
    for elem in lifetime.gameModeStats.squad_fpp:
        print(elem, ':', lifetime.gameModeStats.squad_fpp[elem])
    
def lifetime_json(pubg):
    player_id = ''
    with open('terafiros.json') as data:
        player_id = pubg.get_player_from_json(json.load(data)).id
        
    with open(player_id + '_lifetime_stats.json') as data:
        lifetime = pubg.get_lifetime_stats_from_json(json.load(data))
        for elem in lifetime.gameModeStats.squad_fpp:
            print(elem, ':', lifetime.gameModeStats.squad_fpp[elem])
            
def match_request(pubg):
    match_id = ''
    with open('terafiros.json') as data:
        match_id = pubg.get_player_from_json(json.load(data)).matches[-1]
        
    match = pubg.get_match(match_id)
    print(match.id)
    print(match.mapName)
    print(match.createdAt)
    print(match.duration)
    print(match.gameMode)
    print(match.seasonState)
    print(match.shardId)
    print(match.type)
    print(match.titleId)
    print(match.isCustomMatch)
    print(match.asset)
    for roster in match.rosters:
        print(roster.type)
        print(roster.id)
        print(roster.rank)
        print(roster.teamId)
        print(roster.won)
        print(roster.shardId)
        for part in roster.participants:
            print(part.id)
            print(part.type)
            print(part.shardId)
            print(part.stats)
        

def match_json(pubg):
    match_id = ''
    with open('terafiros.json') as data:
        match_id = pubg.get_player_from_json(json.load(data)).matches[-1]
        
    with open(match_id + '.json') as data:
        match = pubg.get_match_from_json(json.load(data))
        print(match.id)
        print(match.mapName)
        print(match.createdAt)
        print(match.duration)
        print(match.gameMode)
        print(match.seasonState)
        print(match.shardId)
        print(match.type)
        print(match.titleId)
        print(match.isCustomMatch)
        print(match.asset.id)
        print(match.asset.type)
        print(match.asset.name)
        print(match.asset.url)
        print(match.asset.createdAt)
        
        for roster in match.rosters:
            print(roster.type)
            print(roster.id)
            print(roster.rank)
            print(roster.teamId)
            print(roster.won)
            print(roster.shardId)
            for part in roster.participants:
                print(part.id)
                print(part.type)
                print(part.shardId)
                print(part.stats)
    
    
if __name__ == '__main__':
    #sem_api()
    com_api()
    