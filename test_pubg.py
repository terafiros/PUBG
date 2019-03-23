from pygments.lexer import include

from pubg import PUBG, Roster, Participant
import requests



def funcc(included):
    rosters = []

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
                        break

            attrs_r['participants'] = participants
            rosters.append(Roster(**attrs_r))

    return rosters


if __name__ == '__main__':

    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    plat = 'steam'
    pubg = PUBG(key, plat)
    header = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/vnd.api+json'
    }
    url = "https://api.pubg.com/shards/steam/matches/11e5041a-71a5-4612-9587-0ad22cf7b954"
    rsp = requests.get(url, headers=header)

    included = rsp.json()['included']

    rosters = funcc(included)

    player = pubg.get_player('Tecnosh')
    m = pubg.get_match('11e5041a-71a5-4612-9587-0ad22cf7b954')
    print(len(m.rosters))
    count = 0
    for roster in m.rosters:
        count += len(roster.participants)

    print(count)
    print(m.asset.URL)

