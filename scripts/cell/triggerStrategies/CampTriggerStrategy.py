# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class CampTriggerStrategy(TriggerStrategy):
    """
    阵营策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)
        pass

    def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
        super().setInfo(trigger, otherEntity, rangeXZ, rangeY, controllerID, userArg)

    def setData(self, strategyData):
        super().setData(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.getScriptName() == "Avatar":
            if self.otherEntity.getAttr("campName") != self.trigger.getAttr("campName"):
                self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
        elif self.otherEntity.getScriptName() == "Trigger":
            if self.otherEntity.getAttr("campName") != self.trigger.getAttr("campName"):
                self.otherEntity.destroyEntity()
