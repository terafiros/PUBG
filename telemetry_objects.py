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
        
class Vehicle:
    def __init__(self, vehicleType = '', vehicleId = '',
                 healthPercent = 0, feulPercent = 0):
        
        self.vehicleType = vehicleType
        self.vehicleId = vehicleId
        self.healthPercent = healthPercent
        self.feulPercent = feulPercent
        
class GameState:
    def __init__(self, elapsedTime = 0, numAliveTeams = 0,
                 numJoinPlayers = 0, numStartPlayers = 0,
                 numAlivePlayers = 0, safetyZonePosition = None,
                 safetyZoneRadius = 0, poisonGasWarningPosition = None,
                 poisonGasWarningRadius = 0, redZonePosition = None,
                 redZoneRadius = 0):
        
        self.elapsedTime = elapsedTime
        self.numAliveTeams = numAliveTeams
        self.numJoinPlayers = numJoinPlayers
        self.numStartPlayers = numStartPlayers
        self.numAlivePlayers = numAlivePlayers
        self.safetyZonePosition = Location(**safetyZonePosition)
        self.safetyZoneRadius = safetyZoneRadius
        self.poisonGasWarningPosition = Location(**poisonGasWarningPosition)
        self.poisonGasWarningRadius = poisonGasWarningRadius
        self.redZonePosition = Location(**redZonePosition)
        self.redZoneRadius = redZoneRadius

class Item:
    def __init__(self,  itemId = '', stackCount = 0, category = '',
                 subCategory = '', attachedItems = []):
        self.itemId = itemId
        self.stackCount = stackCount
        self.category = category
        self.subCategory = subCategory
        self.attachedItems = attachedItems

class ItemPackage:
    def __init__(self, itemPackageId = '', location = None, items = []):
        self.itemPackageId = itemPackageId
        self.location = Location(**location)
        self.items = items

        
class BlueZoneCustomOptions:
    def __init__(self, phaseNum = 0, startDelay = 0, warningDuration = 0,
                 releaseDuration = 0, poisonGasDamagePerSecond = 0,
                 radiusRate = 0, spreadRatio = 0, landRatio = 0,
                 circleAlgorithm = 0):
        
        self.phaseNum = phaseNum
        self.startDelay = startDelay
        self.warningDuration = warningDuration
        self.releaseDuration = releaseDuration
        self.poisonGasDamagePerSecond = poisonGasDamagePerSecond
        self.radiusRate = radiusRate
        self.spreadRatio = spreadRatio
        self.landRatio = landRatio
        self.circleAlgorithm =  circleAlgorithm
        