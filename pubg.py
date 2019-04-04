import requests
from constants import URLS
from models import Player, Season, PlayerSeasonStats, LifeTimeStats


class PUBG:
    def __init__(self, key, platform):
        self.header = {
            'Authorization': 'Bearer ' + key,
            'Accept': 'application/vnd.api+json'
        }
        self.platform = platform
        self.key = key
                

    def get_player(self, player_name, save_in_json = False):
        
        response = requests.get(URLS.player_url.value.format(platform=self.platform, by='playerNames', value=player_name), headers=self.header)
        player_json = response.json()
        
        if save_in_json:
            file = open(player_name + '.json', 'w+')
            file.write(response.text)
            file.close()
        
        
        return self.get_player_from_json(player_json)
    
    def get_player_from_json(self, player_json):
        attrs = {}
        attrs['name_search_url'] = player_json['links']['self']
        attrs['type'] = player_json['data'][0]['type']
        attrs['id'] = player_json['data'][0]['id']
        attrs['id_search_url'] = player_json['data'][0]['links']['self']
        attrs['titleId'] = player_json['data'][0]['attributes']["titleId"]
        attrs['shardId'] = player_json['data'][0]['attributes']["shardId"]
        attrs['createdAt'] = player_json['data'][0]['attributes']["createdAt"]
        attrs['updatedAt'] = player_json['data'][0]['attributes']["updatedAt"]
        attrs['name'] = player_json['data'][0]['attributes']["name"]

        data_ma = player_json['data'][0]['relationships']['matches']['data']
        matches_id = []
        for ma in data_ma:
            matches_id.append(ma['id'])
            attrs['matches'] = matches_id

        return Player(**attrs)

    def get_seasons(self, save_in_json = False):
        response = requests.get(URLS.seasons_url.value, headers=self.header)
        seasons_json = response.json()
        if save_in_json:
            file = open('seasons.json', 'w+')
            file.write(response.text)
            file.close()
                
        return self.get_seasons_from_json(seasons_json)

    def get_seasons_from_json(self, seasons_json):
        seasons_list = []
        data = seasons_json['data']
        attrs = {}
        for season in data:
            attrs['type'] = season['type']
            attrs['id'] = season['id']
            attrs['isCurrentSeason'] = season['attributes']['isCurrentSeason']
            attrs['isOffseason'] = season['attributes']['isOffseason']
            seasons_list.append(Season(**attrs))

        return seasons_list

    def get_player_stats_for_season(self, player_id, season_id, save_in_json = False):
        response = requests.get(URLS.player_season_url.value.format(playerId=player_id, seasonId=season_id), headers=self.header)
        if save_in_json:
            file = open(player_id + '_' + season_id + '.json', 'w+')
            file.write(response.text)
            file.close()
        
        return self.get_player_stats_for_season_from_json(response.json())
    
    def get_player_stats_for_season_from_json(self, player_season_json):
        return PlayerSeasonStats(player_season_json['data']['attributes']['gameModeStats'])

    
    
    def get_lifetime_stats(self, player_id, save_in_json = False):
        response = requests.get(URLS.lifetime_url.value.format(playerId=player_id),headers=self.header)
        if save_in_json:
            file = open(player_id + '_lifetime_stats.json', 'w+')
            file.write(response.text)
            file.close()
        
        return self.get_lifetime_stats_from_json(response.json())
    
    def get_lifetime_stats_from_json(self, lifetime_json):
         return LifeTimeStats(lifetime_json['data']['attributes']['gameModeStats'])

    def get_match(self, match_id):
        response = requests.get(self.match_url.format(matchId=match_id), headers=self.header)
        attrs = {}
        resp_json = response.json()
        attrs['typee'] = resp_json['data']['type']
        attrs['id'] = resp_json['data']['id']
        attrs['titleId'] = resp_json['data']['attributes']['titleId']
        attrs['shardId'] = resp_json['data']['attributes']['shardId']
        attrs['mapName'] = resp_json['data']['attributes']['mapName']
        attrs['seasonState'] = resp_json['data']['attributes']['seasonState']
        attrs['duration'] = resp_json['data']['attributes']['duration']
        attrs['gameMode'] = resp_json['data']['attributes']['gameMode']
        attrs['isCustomMatch'] = resp_json['data']['attributes']['isCustomMatch']
        attrs['createdAt'] = resp_json['data']['attributes']['createdAt']

        rosters = []
        included = resp_json['included']

        for element in included:
            if element['type'] == 'roster':
                attrs_r = {}
                attrs_r['type'] = 'roster'
                attrs_r['id'] = element['id']
                attrs_r['won'] = element['attributes']['won']
                attrs_r['shard_id'] = element['attributes']['shardId']
                attrs_r['rank'] = element['attributes']['stats']['rank']
                attrs_r['team_id'] = element['attributes']['stats']['teamId']

                participants = []

                for part in element['relationships']['participants']['data']:
                    part_id = part['id']

                    for element in included:
                        if part_id == element['id']:
                            attrs_p = {}
                            attrs_p['type'] = element['type']
                            attrs_p['id'] = element['id']
                            attrs_p['shard_id'] = element['attributes']['shardId']
                            attrs_p['stats'] = element['attributes']['stats']

                            participants.append(Participant(**attrs_p))

                            attrs_r['participants'] = participants
                            rosters.append(Roster(**attrs_r))

            elif element['type'] == 'asset':
                attrs_a = {}
                attrs_a['type'] = 'asset'
                attrs_a['id'] = element['id']
                attrs_a['name'] = element['attributes']['name']
                attrs_a['description'] = element['attributes']['description']
                attrs_a['createdAt'] = element['attributes']['createdAt']
                attrs_a['URL'] = element['attributes']['URL']

                attrs['asset'] = Asset(**attrs_a)


        attrs['rosters'] = rosters
        return Match(**attrs)

        





                

                


class Match:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

class Roster:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
               
class Asset:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
        
class Participant:
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)