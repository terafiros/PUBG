from telemetry.events import *

class Telemetry:

    def __init__(self, telemetry_json, *event_list):
        
        self.events = []
        if len(event_list) > 0:
            for event in telemetry_json:
                for wish_event in event_list:
                    if event['_T'] == wish_event.value:
                        self.events.append(event)
                
        
        else:
            for event in telemetry_json:
                if event['_T'] == 'LogArmorDestroy':
                    self.events.append(ArmorDestroyEvent(**event))
                    
                elif event['_T'] == 'LogCarePackageLand':
                    self.events.append(CarePackageLandEvent(**event))
                    
                elif event['_T'] == 'LogCarePackageSpawn':
                    self.events.append(CarePackageSpawnEvent(**event))               
                
                elif event['_T'] == 'LogGameStatePeriodic':
                    self.events.append(GameStatePeriodicEvent(**event))
                    
                elif event['_T'] == 'LogHeal':
                    self.events.append(HealEvent(**event))
                    
                elif event['_T'] == 'LogItemAttach':
                    self.events.append(ItemAttachEvent(**event))
                    
                elif event['_T'] == 'LogItemDetach':
                    self.events.append(ItemDetachEvent(**event))
                    
                elif event['_T'] == 'LogItemDrop':
                    self.events.append(ItemDropEvent(**event))
                    
                elif event['_T'] == 'LogItemEquip':
                    self.events.append(ItemEquipEvent(**event))
                    
                elif event['_T'] == 'LogItemPickup':
                    self.events.append(ItemPickupEvent(**event))
                    
                elif event['_T'] == 'LogItemPickupFromCarepackage':
                    self.events.append(ItemPickupFromCarePackageEvent(**event))
                    
                elif event['_T'] == 'LogItemPickupFromLootBox':
                    self.events.append(ItemPickupFromLootBoxEvent(**event))
                    
                elif event['_T'] == 'LogItemUnequip':
                    self.events.append(ItemUnequipEvent(**event))
                    
                elif event['_T'] == 'LogItemUse':
                    self.events.append(ItemUseEvent(**event))
                    
                elif event['_T'] == 'LogMatchDefinition':
                    self.events.append(MatchDefinitionEvent(**event))
                    
                elif event['_T'] == 'LogMatchEnd':
                    self.events.append(MatchEndEvent(**event))
                                    
                elif event['_T'] == 'LogMatchStart':
                    self.events.append(MatchStartEvent(**event))
                                    
                elif event['_T'] == 'LogObjectDestroy':
                    self.events.append(ObjectDestroyEvent(**event))
                    
                elif event['_T'] == 'LogParachuteLanding':
                    self.events.append(ParachuteLandingEvent(**event))
                    
                elif event['_T'] == 'LogPlayerAttack':
                    self.events.append(PlayerAttackEvent(**event))
                    
                elif event['_T'] == 'LogPlayerCreate':
                    self.events.append(PlayerCreateEvent(**event))
                    
                elif event['_T'] == 'LogPlayerKill':
                    self.events.append(PlayerKillEvent(**event))
                    
                elif event['_T'] == 'LogPlayerLogin':
                    self.events.append(PlayerLoginEvent(**event))
                    
                elif event['_T'] == 'LogPlayerLogout':
                    self.events.append(PlayerLogoutEvent(**event))           
                
                elif event['_T'] == 'LogPlayerMakeGroggy':
                    self.events.append(PlayerMakeGroggyEvent(**event))
                    
                elif event['_T'] == 'LogPlayerPosition':
                    self.events.append(PlayerPositionEvent(**event))
                    
                elif event['_T'] == 'LogPlayerRevive':
                    self.events.append(PlayerReviveEvent(**event))
                    
                elif event['_T'] == 'LogPlayerTakeDamage':
                    self.events.append(PlayerTakeDamageEvent(**event))
                    
                elif event['_T'] == 'LogRedZoneEnded':
                    self.events.append(RedZoneEndedEvent(**event))
                                    
                elif event['_T'] == 'LogSwimEnd':
                    self.events.append(SwimEndEvent(**event))
                    
                elif event['_T'] == 'LogSwimStart':
                    self.events.append(SwimStartEvent(**event))
                    
                elif event['_T'] == 'LogVaultStart':
                    self.events.append(VaultStartEvent(**event))
            
                elif event['_T'] == 'LogVehicleDestroy':
                    self.events.append(VehicleDestroyEvent(**event))
                    
                elif event['_T'] == 'LogVehicleLeave':
                    self.events.append(VehicleLeaveEvent(**event))

                elif event['_T'] == 'LogVehicleRide':
                    self.events.append(VehicleRideEvent(**event))
                    
                elif event['_T'] == 'LogWeaponFireCount':
                    self.events.append(WeaponFireCountEvent(**event))
                    
                elif event['_T'] == 'LogWheelDestroy':
                    self.events.append(WheelDestroyEvent(**event))
            
            
                    
