from telemetry_objects import *

class ArmorDestroyEvent:
    def __init__(self, attackId = 0, attacker = None,
                 victim = None, damageReason = '',
                 damageTypeCategory = '', damageCauserName = '',
                 item = None, distance = 0, common = None,
                 _D = '', _T = ''):
        self.attackId = attackId
        self.attacker = Character(**attacker)
        self.victim = Character(**victim)
        self.damageReason = damageReason
        self.damageTypeCategory = damageTypeCategory
        self.damageCauserName = damageCauserName
        self.item = Item(**item)
        self.distance = distance
        self.common = Common(**common)
        self._D = _D
        self._T = _T   
        
    def __str__(self):
        return 'LogArmorDestroy'

class CarePackageLandEvent:
    def __init__(self, itemPackage = None, common = None,
                 _D = '', _T = ''):
        
        self.itemPackage = ItemPackage(**itemPackage)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
        
    def __str__(self):
        return 'LogCarePackageLand'
    
class CarePackageSpawnEvent:
    def __init__(self, itemPackage = None, common = None,
                 _D = '', _T = ''):
        
        self.itemPackage = ItemPackage(**itemPackage)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogCarePackageSpawn'


class GameStatePeriodicEvent:
    
    def __init__(self, gameState = None, common = None,
                 _D = '', _T = ''):
        
        self.gameState = GameState(**gameState)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogGameStatePeriodic'


class HealEvent:
    def __init__(self, character = None, item = None,
                  healAmount = 0, common = None,
                 _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.healAmount = healAmount
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    
    
    def __str__(self):
        return 'LogHeal'
    
class ItemAttachEvent:
    
    def __init__(self, character = None, parentItem = None,
                 childItem = None, common = None,
                 _D = '', _T = ''):
        
        self.character = Character(**character)
        self.parentItem = Item(**parentItem)
        self.childItem = Item(**childItem)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogItemAttach'

class ItemDetachEvent:
    
    def __init__(self, character = None, parentItem = None,
                 childItem = None, common = None,
                 _D = '', _T = ''):
        
        self.character = Character(**character)
        self.parentItem = Item(**parentItem)
        self.childItem = Item(**childItem)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
        
    def __str__(self):
        return 'LogItemDetach'

class ItemDropEvent:
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T    
    
    def __str__(self):
        return 'LogItemDrop'

class ItemEquipEvent:
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T      
    
    def __str__(self):
        return 'LogItemEquip'
    
class ItemPickupEvent:
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T        
    
    def __str__(self):
        return 'LogItemPickup'
    

class ItemPickupFromCarePackageEvent:
    
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T     
    
    def __str__(self):
        return 'LogItemPickupFromCarePackage'
    

class ItemPickupFromLootBoxEvent:
    
    def __init__(self, character = None, item = None, ownerTeamId = 0,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.ownerTeamId = ownerTeamId
        self.common = Common(**common)
        self._D = _D
        self._T = _T 
    
    def __str__(self):
        return 'LogItemPickupFromLootBox'

class ItemUnequipEvent:
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T 
    
    def __str__(self):
        return 'LogItemUnequip'
    
class ItemUseEvent:
    def __init__(self, character = None, item = None,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.item = Item(**item)
        self.common = Common(**common)
        self._D = _D
        self._T = _T 
    
    def __str__(self):
        return 'LogItemUse'

class MatchDefinitionEvent:
    def __init__(self, MatchId = '', PingQuality = '',
                 SeasonState = '', _D = '', _T = ''):
        
        self.MatchId = MatchId
        self.PingQuality = PingQuality
        self.SeasonState = SeasonState
        #self.common = Common(**common) not defined
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogMatchDefinition'
    
class MatchEndEvent:
    
    def __init__(self, characters = [], rewardDetail = [],
                 gameResultOnFinished = None,
                 common = None, _D = '', _T = ''):
               
        self.characters = []
        for character in characters:
            self.characters.append(Character(**character))
        
        self.rewardDetail = rewardDetail
        self.common = Common(**common)
        self._D = _D
        self._T = _T
        
    def __str__(self):
        return 'LogMatchEnd'
    
class MatchStartEvent:
    
    def __init__(self, mapName = '', weatherId = '', characters = [],
                 cameraViewBehaviour = '', teamSize = 0, isCustomGame = False,
                 isEventMode = False, blueZoneCustomOptions = '',
                 common = None, _D = '', _T = ''):
        
        self.mapName = mapName
        self.weatherId = weatherId
        self.characters = []
        for character in characters:
            self.characters.append(Character(**character))
        
        self.cameraViewBehaviour = cameraViewBehaviour
        self.teamSize = teamSize
        self.isCustomGame = isCustomGame
        self.isEventMode = isEventMode
        self.blueZoneCustomOptions = blueZoneCustomOptions
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogMatchStart'
    
class ObjectDestroyEvent:
    def __init__(self,character = None, objectType = '',
                 objectLocation = None, common = None,
                 _D = '', _T = ''):
        
        self.character = Character(**character)
        self.objectType = objectType
        self.objectLocation = Location(**objectLocation)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogObjectDestroy'
    
class ParachuteLandingEvent:
    
    def __init__(self, character = None, distance = 0,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.distance = distance
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogParachuteLanding'
    
class PlayerAttack:
    def __str__(self):
        return 'LogPlayerAttack'
    
    
    
    

    



















class PlayerKillEvent:
    def __init__(self, attackId = 0, killer = None, victim = None,
                 assistant = None, dBNOId = 0, damageReason = '',
                 damageTypeCategory = '', damageCauserName = '',
                 damageCauserAdditionalInfo = [], distance = 0,
                 victimGameResult = None, common = None, _D = '', _T = ''):
        
        self.attackId = attackId
        self.killer = Character(**killer)
        self.victim = Character(**victim)
        self.assistant = Character(**assistant)
        self.dBNOId = dBNOId
        self.damageReason = damageReason
        self.damageTypeCategory = damageTypeCategory
        self.damageCauserName = damageCauserName
        self.damageCauserAdditionalInfo = damageCauserAdditionalInfo
        self.distance = distance
        self.victimGameResult = GameResult(**victimGameResult)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
        
    def __str__(self):
        return 'LogPlayerKill'
    
class PlayerPositionEvent:
    def __init__(self, character = None, vehicle = None,
                 elapsedTime = 0, numAlivePlayers = 0,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.vehicle = Vehicle(**vehicle)
        self.elapsedTime = elapsedTime
        self.numAlivePlayers = numAlivePlayers
        self.common = Common(**common)
        self._D = _D
        self._T = _T
        
    def __str__(self):
        return 'LogPlayerPosition'
        
class WeaponFireCountEvent:
    def __init__(self, character = None, weaponId = '',
                 fireCount = 0, common = None, _D = '', _T = ''):
        self.character = Character(**character)
        self.weaponId = weaponId
        self.fireCount = fireCount
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
        
    def __str__(self):
        return 'LogWeaponFireCount'
    
    



    
