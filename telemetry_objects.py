class Character:
    def __init__(self, name = '', teamId = 0, health = 0, location = None,
                 ranking = 0, accountId = '', isInBlueZone = False, isInRedZone = False,
                 zone = []):
        self.name = name
        self.teamId = teamId
        self.health = health
        self.location = Location(**location)
        self.ranking = ranking
        self.accountId = accountId
        self.isInBlueZone = isInBlueZone
        self.zone = zone
        self.isInRedZone = isInRedZone

class Location:
    def __init__(self, x = 0, y = 0, z= 0):
        self.x = x
        self.y = y
        self.z = z

class GameResult:
    def __init__(self, rank = 0, gameResult = '', teamId = 0,
                 stats = None, accountId = ''):
        
        self.rank = rank
        self.gameResult = gameResult
        self.teamId = teamId
        self.stats = Stats(**stats)
        self.accountId = accountId
        
class Stats:
    def __init__(self, killCount = 0, distanceOnFoot = 0, distanceOnSwim = 0,
                 distanceOnVehicle = 0, distanceOnParachute = 0,
                 distanceOnFreefall = 0):
        self.killCount = killCount
        self.distanceOnFoot = distanceOnFoot
        self.distanceOnSwim = distanceOnSwim
        self.distanceOnVehicle = distanceOnVehicle
        self.distanceOnParachute = distanceOnParachute
        self.distanceOnFreefall = distanceOnFreefall
        
class Common:
    def __init__(self, isGame = 0):
        self.isGame = isGame
        
        
        