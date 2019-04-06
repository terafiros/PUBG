from pubg import PUBG
from telemetry_events import *
if __name__ == '__main__':
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    pubg = PUBG(platform='steam', key=key)
    '''
    player = pubg.get_player('terafiros')
    
    last_match = pubg.get_match(player.matches[-1])
    
    print(last_match.asset.name)
    print(last_match.asset.url)
    
    '''
    with open('telemetry.json') as data:
        telemetry_json = pubg.get_telemetry_from_json(data)
        event = telemetry_json[3839]
        print(type(event))
        pke = PlayerKillEvent(**event)
        print(pke.killer.location)
        
    