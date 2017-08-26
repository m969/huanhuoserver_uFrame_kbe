# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class CampStrategy(TriggerStrategy):
    """
    阵营策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)
        pass

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.getScriptName() == "Avatar":
            if self.otherEntity.getAttr("campName") != self.trigger.getAttr("campName"):
                self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
        elif self.otherEntity.getScriptName() == "Trigger":
            if self.otherEntity.getAttr("campName") != self.trigger.getAttr("campName"):
                self.otherEntity.destroyEntity()
