# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class DecelerateStrategy(TriggerStrategy):
    """
    减速策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        DEBUG_MSG("topSpeed " + str(self.otherEntity.topSpeed))
        if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
            if self.otherEntity.getAttr("canReceiveSkill") is True:

                if self.otherEntity.getAttr("canMove") is not None:
                    self.otherEntity.setAttr("topSpeed", self.otherEntity.getAttr("topSpeed") - 4)

                self.otherEntity.addSkillControlTimer(
                    "DecelerateCancelTimer",
                    3,
                    0,
                    "self.topSpeed += 4\n" +
                    "DEBUG_MSG('DecelerateCancelTimer scriptString')",
                    "onceOperation")
