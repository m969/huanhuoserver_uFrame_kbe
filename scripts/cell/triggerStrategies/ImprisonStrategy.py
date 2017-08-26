# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class ImprisonStrategy(TriggerStrategy):
    """
    禁锢策略
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

                if self.otherEntity.getAttr("canMove") is not None:
                    self.otherEntity.moveToPointSample(self.otherEntity.position, 20)
                    self.otherEntity.setAttr("canMove", False)

                if self.otherEntity.getAttr("canCastSkill") is not None:
                    self.otherEntity.setAttr("canCastSkill", False)

                self.otherEntity.addSkillControlTimer(
                    "ImprisonCancelTimer",
                    3,
                    0,
                    "self.canMove = True\n" +
                    "self.canCastSkill = True\n" +
                    "DEBUG_MSG('ImprisonCancelTimer scriptString')",
                    "onceOperation")
