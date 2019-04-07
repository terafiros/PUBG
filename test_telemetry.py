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
     
        for event in telemetry_json:
            
            if event['_T'] == 'LogArmorDestroy':
                ad = ArmorDestroyEvent(**event)
                
            elif event['_T'] == 'LogCarePackageLand':
                cpl = CarePackageLandEvent(**event)
                
            elif event['_T'] == 'LogCarePackageSpawn':
                cps = CarePackageSpawnEvent(**event)                
            
            elif event['_T'] == 'LogGameStatePeriodic':
                gsp = GameStatePeriodicEvent(**event)
                
            elif event['_T'] == 'LogHeal':
                h = HealEvent(**event)
                
            elif event['_T'] == 'LogItemAttach':
                ia = ItemAttachEvent(**event)
                
            elif event['_T'] == 'LogItemDetach':
                id = ItemDetachEvent(**event)
                
            elif event['_T'] == 'LogItemDrop':
                id = ItemDropEvent(**event)
                
            elif event['_T'] == 'LogItemEquip':
                ie = ItemEquipEvent(**event)
                
            elif event['_T'] == 'LogItemPickup':
                ip = ItemPickupEvent(**event)
                
            elif event['_T'] == 'LogItemPickupFromCarepackage':
                ipfcp = ItemPickupFromCarePackageEvent(**event)
                
            
            elif event['_T'] == 'LogItemPickupFromLootBox':
                ipflb = ItemPickupFromLootBoxEvent(**event)
                
            elif event['_T'] == 'LogItemUnequip':
                iu = ItemUnequipEvent(**event)
                
                
            elif event['_T'] == 'LogItemUse':
                iu = ItemUseEvent(**event)
                
            elif event['_T'] == 'LogMatchDefinition':
                md = MatchDefinitionEvent(**event)
                
            elif event['_T'] == 'LogMatchEnd':
                me = MatchEndEvent(**event)
                for c in me.characters:
                    pass
                
            elif event['_T'] == 'LogMatchStart':
                ms = MatchStartEvent(**event)
                for c in ms.characters:
                    pass
                
            elif event['_T'] == 'LogObjectDestroy':
                od = ObjectDestroyEvent(**event)
                
            elif event['_T'] == 'LogParachuteLanding':
                pl = ParachuteLandingEvent(**event)
                print(pl.distance)
                
            
            
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            elif event['_T'] == 'LogPlayerKill':
                pke = PlayerKillEvent(**event)
                
            
            elif event['_T'] == 'LogPlayerPosition':
                ppe = PlayerPositionEvent(**event)
                
            elif event['_T'] == 'LogWeaponFireCount':
                wfc = WeaponFireCountEvent(**event)
                
            
                
            elif event['_T'] == 'LogCarePackageLand':
                cpl = CarePackageLandEvent(**event)            
 
 
