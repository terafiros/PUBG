from enum import Enum

class URLS(Enum):
    
    player_url = 'https://api.pubg.com/shards/{platform}/players?filter[{by}]={value}'
    seasons_url = 'https://api.pubg.com/shards/{platform}/seasons'
    
    
    player_season_url = 'https://api.pubg.com/shards/{platform}/players/{playerId}/seasons/{seasonId}'
    lifetime_url = 'https://api.pubg.com/shards/{platform}/players/{playerId}/seasons/lifetime'
    
    match_url = 'https://api.pubg.com/shards/{platform}/matches/{matchId}'
    sample_url = 'https://api.pubg.com/shards/{platform}/samples'
    
    leaderboard_url = 'https://api.pubg.com/shards/{platform}/leaderboards/{gameMode}?page[number]={pageNumber}'
    tournaments_url = 'https://api.pubg.com/tournaments/{id}'
    
    status_url = 'https://api.pubg.com/status'

class Events(Enum):
    
    LogArmorDestroy = 'LogArmorDestroy'
    LogCarePackageLand = 'LogCarePackageLand'
    LogCarePackageSpawn = 'LogCarePackageSpawn'
    LogGameStatePeriodic = 'LogGameStatePeriodic'
    LogHeal = 'LogHeal'
    
    LogItemAttach = 'LogItemAttach'
    LogItemDetach = 'LogItemDetach'
    LogItemDrop = 'LogItemDrop'
    LogItemEquip = 'LogItemEquip'
    LogItemPickup = 'LogItemPickup'
    
    LogItemPickupFromCarepackage = 'LogItemPickupFromCarepackage'
    LogItemPickupFromLootbox = 'LogItemPickupFromLootbox'
    LogItemUnequip = 'LogItemUnequip'
    LogItemUse = 'LogItemUse'
    LogMatchDefinition = 'LogMatchDefinition'
    
    LogMatchEnd = 'LogMatchEnd'
    LogMatchStart = 'LogMatchStart'
    LogObjectDestroy = 'LogObjectDestroy'
    LogParachuteLanding = 'LogParachuteLanding'
    LogPlayerAttack = 'LogPlayerAttack'
    
    LogPlayerCreate = 'LogPlayerCreate'
    LogPlayerKill = 'LogPlayerKill'
    LogPlayerLogin = 'LogPlayerLogin'
    LogPlayerLogout = 'LogPlayerLogout'
    LogPlayerMakeGroggy = 'LogPlayerMakeGroggy'
    
    LogPlayerPosition = 'LogPlayerPosition'
    LogPlayerRevive = 'LogPlayerRevive'
    LogPlayerTakeDamage = 'LogPlayerTakeDamage'
    LogRedZoneEnded = 'LogRedZoneEnded'
    LogSwimEnd = 'LogSwimEnd'
    
    LogSwimStart = 'LogSwimStart'
    LogVaultStart = 'LogVaultStart'
    LogVehicleDestroy = 'LogVehicleDestroy'
    LogVehicleLeave = 'LogVehicleLeave'
    LogVehicleRide = 'LogVehicleRide'
    
    LogWeaponFireCount = 'LogWeaponFireCount'
    LogWheelDestroy = 'LogWheelDestroy'
    
class Shard(Enum):
    pc = 'steam'
    pc_as = 'pc-as' # Asia
    pc_eu = 'pc-eu'# Europe
    pc_jp = 'pc-jp'# Japan
    pc_kakao = 'pc-kakao'# Kakao
    kakao = 'kakao'
    pc_krjp = 'pc-krjp'# Korea
    pc_na = 'pc-na'# North America
    pc_oc = 'pc-oc'# Oceania
    pc_ru = 'pc-ru'# Russia
    pc_sa = 'pc-sa'# South and Central America
    pc_sea = 'pc-sea'# South East Asia
    pc_tournament = 'pc-tournament'# Tournaments
    psn = 'psn'
    psn_as = 'psn-as'# Asia
    psn_eu = 'psn-eu'# Europe
    psn_na = 'psn-na'# North America
    psn_oc = 'psn-oc'# Oceania
    xbox = 'xbox'
    xbox_as = 'xbox-as'# Asia
    xbox_eu = 'xbox-eu'# Europe
    xbox_na = 'xbox-na'# North America
    xbox_oc = 'xbox-oc'# Oceania
    xbox_sa = 'xbox-sa'# South America
    

