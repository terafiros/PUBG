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

class GameModeStats:
    def __init__(self, gameModeStats):
        self.duo = gameModeStats['duo']
        self.duo_fpp = gameModeStats['duo-fpp']
        self.solo = gameModeStats['solo']
        self.solo_fpp = gameModeStats['solo-fpp']
        self.squad = gameModeStats['squad']
        self.squad_fpp = gameModeStats['squad-fpp']        

class PlayerSeasonStats:
    def __init__(self, gameModeStats):
        self.gameModeStats = GameModeStats(gameModeStats)
        
class LifeTimeStats:
    def __init__(self, gameModeStats):
        self.gameModeStats = GameModeStats(gameModeStats)

class Match:
    def __init__(self, type = '', id = '', createdAt = '', duration = 0, gameMode = '', mapName = '', isCustomMatch = False, seasonState = '', shardId = '', titleId = '', asset = None, rosters = []):
        self.type = type
        self.id = id
        self.createdAt = createdAt
        self.duration = duration
        self.gameMode = gameMode
        self.mapName = mapName
        self.isCustomMatch =  isCustomMatch
        self.seasonState = seasonState
        self.shardId = shardId
        self.titleId = titleId
        self.asset = asset
        self.rosters = rosters

class Roster:
    def __init__(self, type = '', id = '', rank = 0, teamId = 0, won = False, shardId = '', participants = []):
        self.type = type
        self.id = id
        self.rank = rank
        self.teamId = teamId
        self.won = won
        self.shardId = shardId
        self.participants = participants

class Participant:
    def __init__(self, type = '', id = '', shardId = '', stats = {}):
        self.type = type
        self.id = id
        self.shardId = shardId
        self.stats = stats

class Asset:
    def __init__(self, type = '', id = '', url = '', createdAt = '', name = ''):
        self.type = type
        self.id = id
        self.url = url
        self.createdAt = createdAt
        self.name = name

class Sample:
    def __init__(self, type = '', id ='', titleId = '', shardId = '', createdAt = '', matches = []):
        self.type = type
        self.id = id
        self.titleId = titleId
        self.shardId = shardId
        self.createdAt = createdAt
        self.matches = matches