from pubg import PUBG
import json

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
        print(player.matches)
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
    
def sample_request(pubg):
    sample = pubg.get_sample()
    print(sample.id)
    print(sample.type)
    print(sample.createdAt)
    print(sample.shardId)
    print(sample.titleId)
    print(len(sample.matches))
    

def sample_json(pubg):
    with open('sample.json') as data:
        sample = pubg.get_sample_from_json(json.load(data))
        print(sample.id)
        print(sample.type)
        print(sample.createdAt)
        print(sample.shardId)
        print(sample.titleId)
        print(len(sample.matches))
        
def leaderboard_request(pubg):
    pass    

def leaderboard_json(pubg):
    pass
        
def tournaments_request(pubg):
    tournaments = pubg.get_tournaments()
    print(len(tournaments))
    for t in tournaments:
        print(t)
    
    tournament = pubg.get_tournaments(tournament_id='sea-vnlpt')
        
    print(tournament.type)
    print(tournament.id)
    print(tournament.urlLink)
    
    print(len(tournament.matches))
    for match in tournament.matches:
        print(match)

def tournaments_json(pubg):
    with open('tournaments.json') as data:
        tournaments = pubg.get_tournaments_from_json(json.load(data))
        print(len(tournaments))
        for t in tournaments:
            print(t)
    
    with open('tournaments.json') as data:
        tournament_id = pubg.get_tournaments_from_json(json.load(data))[0]
        with open(tournament_id + '_tournaments.json') as data:
            tournament = pubg.get_tournaments_from_json(json.load(data), all_tournaments=False)
            print(tournament.type)
            print(tournament.id)
            print(tournament.urlLink)
    
            print(len(tournament.matches))
            for match in tournament.matches:
                print(match)
            
def api_simple_queries():
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    '''
    player_request(pubg)
    player_json(pubg)
    
    seasons_request(pubg)
    seasons_json(pubg)
    
    player_season_stats_request(pubg)
    player_season_stats_json(pubg)
    
    lifetime_request(pubg)
    lifetime_json(pubg)
    
    match_request(pubg)
    match_json(pubg)
    
    sample_request(pubg)
    sample_json(pubg)
    
    #no server answer
    leaderboard_request(pubg)
    leaderboard_json(pubg)
    
    tournaments_request(pubg)
    tournaments_json(pubg)
    '''
if __name__ == '__main__':
    api_simple_queries()
    
    