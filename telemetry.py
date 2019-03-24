class Telemetry:

    def __init__(self, telametry_json):
        self.telemetry_json = telametry_json

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