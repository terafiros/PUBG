class Player:
    def __init__(self, type = '', id = '', updatedAt = '', name = '', titleId = '', shardId = '', createdAt = '', matches = [], name_search_url = '', id_search_url = '' ):
        self.type = type
        self.id = id
        self.updatedAt = updatedAt
        self.name = name
        self.titleId = titleId
        self.shardId = shardId
        self.createdAt = createdAt
        self.matches = matches
        self.name_search_url = name_search_url
        self.id_search_url = id_search_url

class Season:
    def __init__(self, type = '', id = '', isOffseason = False, isCurrentSeason = False):
        self.id = id
        self.type = type
        self.isOffseason = isOffseason
        self.isCurrentSeason = isCurrentSeason
        
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