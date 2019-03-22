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

        def get_player(self, player_name):
                response = requests.get(self.player_url.format(platform=self.platform, by='playerNames', value=player_name), headers=self.header)
                player_json = response.json()

                return self.json_2_player(player_json)

        def json_2_player(self, player_json):
                linkss = player_json['links']
                attrs = {}
                attrs['url_name_search'] = linkss['self']

                datas = player_json['data']
                datas_dict = datas[0]
                attrs['typee'] = datas_dict['type']
                attrs['idd'] = datas_dict['id']
                links = datas_dict['links']
                attrs['url_id_search'] = links['self']
                attributes = datas_dict['attributes']
                attrs['titleId'] = attributes["titleId"]
                attrs['shardId'] = attributes["shardId"]
                attrs['createdAt'] = attributes["createdAt"]
                attrs['updatedAt'] = attributes["updatedAt"]
                attrs['name'] = attributes["name"]

                relationships = datas_dict['relationships']
                matches = relationships['matches']
                data_ma = matches['data']

                matches_id = []
                for ma in data_ma:
                        matches_id.append(ma['id'])

                attrs['matches_id'] = matches_id

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

class Player:
        def __init__(self, **kwargs):
                for attribute, value in kwargs.items():
                        setattr(self, attribute, value)


class Season:
         def __init__(self, **kwargs):
                for attribute, value in kwargs.items():
                        setattr(self, attribute, value)



