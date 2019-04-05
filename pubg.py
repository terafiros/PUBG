import requests
from constants import URLS
from models import Player, Season, PlayerSeasonStats, LifeTimeStats, Match, Roster, Participant, Asset, Sample


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
        response = requests.get(URLS.seasons_url.value.format(platform=self.platform), headers=self.header)
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
        response = requests.get(URLS.player_season_url.value.format(platform=self.platform,playerId=player_id, seasonId=season_id), headers=self.header)
        if save_in_json:
            file = open(player_id + '_' + season_id + '.json', 'w+')
            file.write(response.text)
            file.close()
        
        return self.get_player_stats_for_season_from_json(response.json())
    
    def get_player_stats_for_season_from_json(self, player_season_json):
        return PlayerSeasonStats(player_season_json['data']['attributes']['gameModeStats'])

    
    
    def get_lifetime_stats(self, player_id, save_in_json = False):
        response = requests.get(URLS.lifetime_url.value.format(platform=self.platform, playerId=player_id),headers=self.header)
        if save_in_json:
            file = open(player_id + '_lifetime_stats.json', 'w+')
            file.write(response.text)
            file.close()
        
        return self.get_lifetime_stats_from_json(response.json())
    
    def get_lifetime_stats_from_json(self, lifetime_json):
        return LifeTimeStats(lifetime_json['data']['attributes']['gameModeStats'])

    def get_match(self, match_id, save_in_json = False):
        response = requests.get(URLS.match_url.value.format(platform=self.platform, matchId=match_id), headers=self.header)
        if save_in_json:
            file = open(match_id + '.json', 'w+')
            file.write(response.text)
            file.close()
            
        return self.get_match_from_json(response.json())
            
        
    
    def get_match_from_json(self, match_json):
        attrs = {}
        attrs['type'] = match_json['data']['type']
        attrs['id'] = match_json['data']['id']
        attrs['titleId'] = match_json['data']['attributes']['titleId']
        attrs['shardId'] = match_json['data']['attributes']['shardId']
        attrs['mapName'] = match_json['data']['attributes']['mapName']
        attrs['seasonState'] = match_json['data']['attributes']['seasonState']
        attrs['duration'] = match_json['data']['attributes']['duration']
        attrs['gameMode'] = match_json['data']['attributes']['gameMode']
        attrs['isCustomMatch'] = match_json['data']['attributes']['isCustomMatch']
        attrs['createdAt'] = match_json['data']['attributes']['createdAt']

        rosters = []
        included = match_json['included']

        for element in included:
            if element['type'] == 'roster':
                attrs_r = {}
                attrs_r['type'] = 'roster'
                attrs_r['id'] = element['id']
                attrs_r['won'] = element['attributes']['won']
                attrs_r['shardId'] = element['attributes']['shardId']
                attrs_r['rank'] = element['attributes']['stats']['rank']
                attrs_r['teamId'] = element['attributes']['stats']['teamId']

                participants = []

                for part in element['relationships']['participants']['data']:
                    part_id = part['id']

                    for element in included:
                        if part_id == element['id']:
                            attrs_p = {}
                            attrs_p['type'] = element['type']
                            attrs_p['id'] = element['id']
                            attrs_p['shardId'] = element['attributes']['shardId']
                            attrs_p['stats'] = element['attributes']['stats']

                            participants.append(Participant(**attrs_p))

                            attrs_r['participants'] = participants
                            rosters.append(Roster(**attrs_r))

            elif element['type'] == 'asset':
                attrs_a = {}
                attrs_a['type'] = 'asset'
                attrs_a['id'] = element['id']
                attrs_a['name'] = element['attributes']['name']
                attrs_a['createdAt'] = element['attributes']['createdAt']
                attrs_a['url'] = element['attributes']['URL']

                attrs['asset'] = Asset(**attrs_a)


        attrs['rosters'] = rosters
        return Match(**attrs)
    
    def get_sample(self, save_in_json = False):
        response = requests.get(URLS.sample_url.value.format(platform=self.platform), headers=self.header)
        if save_in_json:
            file = open('sample.json', 'w+')
            file.write(response.text)
            file.close()
            
        return self.get_sample_from_json(response.json())
    
    def get_sample_from_json(self, sample_json):
        attrs = {}
        attrs['type'] = sample_json['data']['type']
        attrs['id'] = sample_json['data']['id'] 
        attrs['titleId'] = sample_json['data']['attributes']['titleId']
        attrs['shardId'] = sample_json['data']['attributes']['shardId']
        attrs['createdAt'] = sample_json['data']['attributes']['createdAt']
        matches = []
        for match in sample_json['data']['relationships']['matches']['data']:
            matches.append(match['id'])
        
        attrs['matches'] = matches
        
        return Sample(**attrs)
        
    
    