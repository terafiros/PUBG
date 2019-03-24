import requests


class PUBG:
        def __init__(self, key, platform):
                self.header = {
                        'Authorization': 'Bearer ' + key,
                        'Accept': 'application/vnd.api+json'
                }
                self.platform = platform
                self.player_url = 'https://api.pubg.com/shards/{platform}/players?filter[{by}]={value}'
                self.seasons_url = 'https://api.pubg.com/shards/steam/seasons'
                self.player_season_url = 'https://api.pubg.com/shards/steam/players/{playerId}/seasons/{seasonId}'
                self.lifetime_url = 'https://api.pubg.com/shards/steam/players/{playerId}/seasons/lifetime'
                self.match_url = 'https://api.pubg.com/shards/steam/matches/{matchId}'

        def get_player(self, player_name):
                response = requests.get(self.player_url.format(platform=self.platform, by='playerNames', value=player_name), headers=self.header)
                player_json = response.json()
                return self.json_2_player(player_json)

        def json_2_player(self, player_json):
                attrs = {}
                attrs['url_name_search'] = player_json['links']['self']
                attrs['type'] = player_json['data'][0]['type']
                attrs['id'] = player_json['data'][0]['id']
                attrs['url_id_search'] = player_json['data'][0]['links']['self']
                attrs['titleId'] = player_json['data'][0]['attributes']["titleId"]
                attrs['shardId'] = player_json['data'][0]['attributes']["shardId"]
                attrs['createdAt'] = player_json['data'][0]['attributes']["createdAt"]
                attrs['updatedAt'] = player_json['data'][0]['attributes']["updatedAt"]
                attrs['name'] = player_json['data'][0]['attributes']["name"]

                data_ma = player_json['data'][0]['relationships']['matches']['data']
                matches_id = []
                for ma in data_ma:
                        matches_id.append(ma['id'])

                attrs['matches_ids'] = matches_id

                return Player(**attrs)

        def get_seasons(self):
                response = requests.get(self.seasons_url, headers=self.header)
                seasons_json = response.json()
                
                return self.create_seasons_list(seasons_json)

        def create_seasons_list(self, seasons_json):
                seasons_list = []
                data = seasons_json['data']
                attrs = {}
                for season in data:
                    attrs['typee'] = season['type']
                    attrs['idd'] = season['id']
                    attrs['isCurrentSeason'] = season['attributes']['isCurrentSeason']
                    attrs['isOffseason'] = season['attributes']['isOffseason']
                    seasons_list.append(Season(**attrs))

                return seasons_list

        def get_player_stats_for_season(self, player_id, season_id):
                response = requests.get(self.player_season_url.format(playerId=player_id, seasonId=season_id), headers=self.header)
                return PlayerSeasonStats(response.json()['data']['attributes']['gameModeStats'])


        def get_lifetime_stats(self, player_id):
                response = requests.get(self.lifetime_url.format(playerId=player_id),headers=self.header)
                return LifeTimeStats(response.json()['data']['attributes']['gameModeStats'])

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

        
class Player:   
        def __init__(self, **kwargs):
                for attribute, value in kwargs.items():
                        setattr(self, attribute, value)


class Season:
         def __init__(self, **kwargs):
                for attribute, value in kwargs.items():
                        setattr(self, attribute, value)


class PlayerSeasonStats:
        def __init__(self, gameModeStats):
                self.gameModeStats = GameModeStats(gameModeStats)
                
class GameModeStats:
        def __init__(self, gameModeStats):
                self.duo = gameModeStats['duo']
                self.duo_fpp = gameModeStats['duo-fpp']
                self.solo = gameModeStats['solo']
                self.solo_fpp = gameModeStats['solo-fpp']
                self.squad = gameModeStats['squad']
                self.squad_fpp = gameModeStats['squad-fpp']
                
class LifeTimeStats:
        def __init__(self, gameModeStats):
                self.gameModeStats = GameModeStats(gameModeStats)

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