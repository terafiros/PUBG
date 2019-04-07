from core.pubg import PUBG
import time, json

if __name__ == '__main__':
    key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwMDQzNWU1MC0xODZiLTAxMzctNzM1OC0wZTM1MzFmZGJkNWEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUwNzk3MTU2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctdGVhY2hlciJ9.zM2r5FJZP3IkcRVVFN1ApBDesf-JJn3QPAZyxNr2QR4'
    pubg = PUBG(platform='steam', key=key)
    
    '''
    to download a asset/telemtry file
    
    player = pubg.get_player('terafiros')
    last_match = pubg.get_match(player.matches[-1])
    print(last_match.asset.name)
    print(last_match.asset.url)
    
    '''
    
    with open('json/telemetry.json') as data:
        
        telemetry_json = json.load(data)
        start = time.time()
        telemetry = pubg.get_telemetry_from_json(telemetry_json)    
        end = time.time()
        print(end - start)
        print(len(telemetry.events))
        
        
        
        
    #pubg.get_status()
'''
    def player_kill(self, player_name = []):
        if len(player_name) == 0:
            positions = []
            for tele in self.telemetry_json:
                if tele['_T'] == 'LogPlayerKill':

                    x = tele['victim']['location']['x']
                    y = tele['victim']['location']['y']

                    ox = 8000 * x / 816000
                    oy = 8000 * y / 816000

                    positions.append((ox, oy))

            return positions

        elif len(player_name) > 0:
                positions = []
                log_player_kill = []
                for tele in self.telemetry_json:
                    if tele['_T'] == 'LogPlayerKill':
                        log_player_kill.append(tele)

                for name in player_name:
                    for log in log_player_kill:
                        if name == log['killer']['name']:
                            x = log['victim']['location']['x']
                            y = log['victim']['location']['y']

                            ox = 8000 * x / 816000
                            oy = 8000 * y / 816000

                            positions.append((ox, oy))

                return positions


    def safety_zone_position(self):
        positions = []
        verify = 0
        for telemetry in self.telemetry_json:
            if telemetry['_T'] == 'LogGameStatePeriodic':
                if telemetry['common']['isGame'] > verify:

                    verify += 1
                    safe_x = telemetry['gameState']['safetyZonePosition']['x']
                    safe_y = telemetry['gameState']['safetyZonePosition']['y']
                    radius = telemetry['gameState']['safetyZoneRadius']
    
                    safe_ox = 8000 * safe_x / 816000
                    safe_oy = 8000 * safe_y / 816000
                    radius_o = 8000 * radius / 816000

                    positions.append((safe_ox, safe_oy, radius_o))

        return positions
'''