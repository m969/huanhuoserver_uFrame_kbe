# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class OnceDamageStrategy(TriggerStrategy):
    """
    一次伤害策略
    """

    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.getAttr("canDamage") is True:
            if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
                self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
                self.trigger.destroy()
