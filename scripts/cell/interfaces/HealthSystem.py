# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class HealthSystem:
    def __init__(self):
        DEBUG_MSG("HealthSystem:__init__")
        self.canAttack = True
        self.canDamage = True
        self.canHealth = True
        self.HP = self.HP_Max

    def onTimer(self, timerHandle, userData):
        if userData == 21:  # 重生定时器
            DEBUG_MSG("Avatar set respawnPosition!")
            respawnPosition = self.getCurrSpace().getAttr("respawnPoint")
            DEBUG_MSG(respawnPosition)
            self.position = respawnPosition
            self.HP = self.HP_Max
            self.MSP = self.MSP_Max
            self.SP = self.SP_Max
            self.allClients.OnRespawn(respawnPosition)
            self.delTimer(timerHandle)

    def receiveDamage(self, attackerMailbox, damage):
        DEBUG_MSG("HealthSystem:receiveDamage")
        oldHP = self.HP
        if damage >= self.HP:
            self.HP = 0
        else:
            self.HP -= damage
        if oldHP != self.HP:
            self.onHPChange(attackerMailbox)

    def onHPChange(self, murderer):
        if self.HP <= 0:
            self.dieSelf(murderer)

    def dieSelf(self, murderer):
        self.onDie(murderer)

    def onDie(self, murderer):
        DEBUG_MSG("HealthSystem:onDie")
        self.addTimer(4, 0, 21)  # 添加重生时间器
        self.allClients.OnDie()
