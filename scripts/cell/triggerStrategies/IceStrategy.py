# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class IceStrategy(TriggerStrategy):
    """
    冰霜策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
            if self.otherEntity.getAttr("canReceiveSkill") is True:
                self.otherEntity.setAttr("isIceFreezing", True)
                self.otherEntity.addSkillControlTimer(
                    "IceCancelTimer",
                    3,
                    0,
                    "self.isIceFreezing = False\n" +
                    "DEBUG_MSG('IceCancelTimer scriptString')",
                    "onceOperation")
