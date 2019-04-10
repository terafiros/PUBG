from telemetry.objects import *

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
    
class PlayerAttackEvent:
    
     def __init__(self, attackId = 0, fireWeaponStackCount = 0,
                  attacker = None, attackType = '', weapon = None,
                  vehicle = None, common = None, _D = '', _T = ''):
         
         self.attackId = attackId
         self.fireWeaponStackCount = fireWeaponStackCount
         self.attacker = Character(**attacker)
         self.attackType = attackType
         self.weapon = Item(**weapon)
         
         if vehicle == None:
             self.vehicle = None
         else:
             self.vehicle = Vehicle(**vehicle)
         self.common = Common(**common)
         self._D = _D
         self._T = _T
    
     def __str__(self):
         return 'LogPlayerAttack'
        
class PlayerCreateEvent:
    
    def __init__(self, character = None,
                 common = None, _D = '', _T = ''):
         
         self.character = Character(**character)
         self.common = Common(**common)
         self._D = _D
         self._T = _T
    
    def __str__(self):
         return 'LogPlayerCreate'
    
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
    
    
class PlayerLoginEvent:
    
    def __init__(self, accountId = '',
                 common = None, _D = '', _T = ''):
        
        self.accountId = accountId
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogPlayerLogin'
    
    
    
class PlayerLogoutEvent:
    def __init__(self, accountId = '',
                 common = None, _D = '', _T = ''):
        
        self.accountId = accountId
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogPlayerLogout'
    
class PlayerMakeGroggyEvent:
    
    def __init__(self, attackId = 0, attacker = None, victim = None,
                 dBNOId = 0, damageReason = '', damageTypeCategory = '',
                 damageCauserName = '', damageCauserAdditionalInfo = [],
                 distance = 0, isAttackerInVehicle = False,
                 common = None, _D = '', _T = ''):
        
        self.attackId = attackId
        self.attacker = Character(**attacker)
        self.victim = Character(**victim)
        self.dBNOId = dBNOId
        self.damageReason = damageReason
        self.damageTypeCategory = damageTypeCategory
        self.damageCauserName = damageCauserName
        self.damageCauserAdditionalInfo = damageCauserAdditionalInfo
        self.distance = distance
        self.isAttackerInVehicle = isAttackerInVehicle
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogPlayerMakeGroggy'
    
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
    
class PlayerReviveEvent:
    
    def __init__(self, reviver = None, victim = None,
                 dBNOId = 0, common = None, _D = '', _T = ''):
        
        self.reviver = Character(**reviver)
        self.victim = Character(**victim)
        self.dBNOId = dBNOId
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogPlayerRevive'
    
class PlayerTakeDamageEvent:
    
    def __init__(self, attackId = 0, attacker = None, victim = None,
                 damageReason = '', damageTypeCategory = '',
                 damageCauserName = '', damage = 0,
                 common = None, _D = '', _T = ''):
        
        self.attackId = attackId
        if attacker == None:
            self.attacker = None            
        else:
            self.attacker = Character(**attacker)
            
        self.victim = Character(**victim)
        self.damageReason = damageReason
        self.damageTypeCategory = damageTypeCategory
        self.damageCauserName = damageCauserName        
        self.damage = damage
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogPlayerTakeDamage'
    
class RedZoneEndedEvent:
    
    def __init__(self, drivers = [],
                 common = None, _D = '', _T = ''):
               
        self.drivers = []
        for driver in drivers:
            self.drivers.append(Character(**driver))
        
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogRedZoneEnded'
    
class SwimEndEvent:
    
    def __init__(self, character = None,
                 swimDistance = 0, maxSwimDepthOfWater = 0,
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.swimDistance = swimDistance
        self.maxSwimDepthOfWater = maxSwimDepthOfWater
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogSwimEnd'

class SwimStartEvent:
    
    def __init__(self, character = None, 
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogSwimStart'
    
class VaultStartEvent:
    
    def __init__(self, character = None, 
                 common = None, _D = '', _T = ''):
        
        self.character = Character(**character)
        self.common = Common(**common)
        self._D = _D
        self._T = _T
    
    def __str__(self):
        return 'LogVaultStart'
    
    
    
class VehicleDestroyEvent:
    def __init__(self, attackId = 0, attacker = None, vehicle = None,
                     damageTypeCategory = '', damageCauserName = '',
                     distance = 0, common = None, _D = '', _T = ''):
            
            self.attackId = attackId
            self.attacker = Character(**attacker)
            self.vehicle = Vehicle(**vehicle)
            self.damageTypeCategory = damageTypeCategory
            self.damageCauserName = damageCauserName        
            self.distance = distance
            self.common = Common(**common)
            self._D = _D
            self._T = _T
    
    def __str__(self):
        return 'LogVehicleDestroy'
        
    
class VehicleLeaveEvent:
    def __init__(self, character = None, vehicle = None,
                     rideDistance = 0, seatIndex = 0,
                     maxSpeed = 0, common = None, _D = '', _T = ''):
            
            
            self.character = Character(**character)
            self.vehicle = Vehicle(**vehicle)
            self.rideDistance = rideDistance
            self.seatIndex = seatIndex        
            self.maxSpeed = maxSpeed
            self.common = Common(**common)
            self._D = _D
            self._T = _T
    
    def __str__(self):
        return 'LogVehicleLeave'

class VehicleRideEvent:
    def __init__(self, character = None, vehicle = None,
                 seatIndex = 0, common = None, _D = '', _T = ''):
            
            
            self.character = Character(**character)
            self.vehicle = Vehicle(**vehicle)
            self.seatIndex = seatIndex        
            self.common = Common(**common)
            self._D = _D
            self._T = _T
    
    def __str__(self):
        return 'LogVehicleRide'
    
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
    
class WheelDestroyEvent:
    def __init__(self, attackId = 0, attacker = None, vehicle = None,
                     damageTypeCategory = '', damageCauserName = '',
                     common = None, _D = '', _T = ''):
            
            self.attackId = attackId
            self.attacker = Character(**attacker)
            self.vehicle = Vehicle(**vehicle)
            self.damageTypeCategory = damageTypeCategory
            self.damageCauserName = damageCauserName
            self.common = Common(**common)
            self._D = _D
            self._T = _T
    
    def __str__(self):
        return 'LogWheelDestroy'
    
class EventFactory:
    
    def get_event(self, event, **attributes):
        if event == 'LogArmorDestroy':
            return ArmorDestroyEvent(**attributes)
        
        elif  event == 'LogCarePackageLand':
            return CarePackageLandEvent(**attributes)
        
        elif  event == 'LogCarePackageSpawn':
            return CarePackageSpawnEvent(**attributes)
        
        elif  event == 'LogGameStatePeriodic':
            return GameStatePeriodicEvent(**attributes)
        
        elif  event == 'LogHeal':
            return HealEvent(**attributes)
        
        elif  event == 'LogItemAttach':
            return ItemAttachEvent(**attributes)
        
        elif  event == 'LogItemDetach':
            return ItemDetachEvent(**attributes)
        
        elif   event == 'LogItemDrop':
            return ItemDropEvent(**attributes)
        
        elif   event == 'LogItemEquip':
            return ItemEquipEvent(**attributes)
        
        elif   event == 'LogItemPickup':
            return ItemPickupEvent(**attributes)
        
        elif   event == 'LogItemPickupFromCarepackage':
            return ItemPickupFromCarePackageEvent(**attributes)
        
        elif   event == 'LogItemPickupFromLootbox':
            return ItemPickupFromLootBoxEvent(**attributes)
        
        elif   event == 'LogItemUnequip':
            return ItemUnequipEvent(**attributes)
        
        elif   event == 'LogItemUse':
            return ItemUseEvent(**attributes)
        
        elif     event == 'LogMatchDefinition':
            return MatchDefinitionEvent(**attributes)
        
        elif     event == 'LogMatchEnd':
            return MatchEndEvent(**attributes)
        
        elif   event == 'LogMatchStart':
            return MatchStartEvent(**attributes)
        
        elif   event == 'LogObjectDestroy':
            return ObjectDestroyEvent(**attributes)
        
        elif   event == 'LogParachuteLanding':
            return ParachuteLandingEvent(**attributes)
        
        elif   event == 'LogPlayerAttack':
            return PlayerAttackEvent(**attributes)
        
        elif   event == 'LogPlayerCreate':
            return PlayerCreateEvent(**attributes)
        
        elif event == 'LogPlayerKill':
            return PlayerKillEvent(**attributes)
        
        elif   event == 'LogPlayerLogin':
            return PlayerLoginEvent(**attributes)
        
        elif   event == 'LogPlayerLogout':
            return PlayerLogoutEvent(**attributes)
         
        elif event == 'LogPlayerMakeGroggy':
            return PlayerMakeGroggyEvent(**attributes)
        
        elif event == 'LogPlayerPosition':
            return PlayerPositionEvent(**attributes)
        
        elif event == 'LogPlayerRevive':
            return PlayerReviveEvent(**attributes)
        
        elif event == 'LogPlayerTakeDamage':
            return PlayerTakeDamageEvent(**attributes)
        
        elif event == 'LogRedZoneEnded':
            return RedZoneEndedEvent(**attributes)
        
        elif event == 'LogSwimEnd':
            return SwimEndEvent(**attributes)
        
        elif event == 'LogVaultStart':
            return VaultStartEvent(**attributes)
        
        elif   event == 'LogVehicleDestroy':
            return VehicleDestroyEvent(**attributes)
        
        elif   event == 'LogVehicleLeave':
            return VehicleLeaveEvent(**attributes)
        
        elif   event == 'LogVehicleRide':
            return VehicleRideEvent(**attributes)
        
        elif   event == 'LogWeaponFireCount':
            return WeaponFireCountEvent(**attributes)
        
        elif   event == 'LogWheelDestroy':
            return WheelDestroyEvent(**attributes)