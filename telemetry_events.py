from telemetry_objects import *

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
        
    