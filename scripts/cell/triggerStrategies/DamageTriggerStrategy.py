# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class DamageTriggerStrategy(TriggerStrategy):
    """
    伤害策略
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
        # if self.otherEntity.getAttr("className") == self.trigger.owner.getAttr("className"):
        #     return
        if self.otherEntity.getAttr("canDamage") is True:
            if self.otherEntity.getEntityID() != self.trigger.owner.getEntityID():
                if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
                    self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
