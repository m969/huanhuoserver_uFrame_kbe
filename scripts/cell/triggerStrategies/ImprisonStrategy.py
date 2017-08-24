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

    def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
        super().setInfo(trigger, otherEntity, rangeXZ, rangeY, controllerID, userArg)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self):
        super().execute()
        if self.otherEntity.getEntityID() != self.trigger.owner.getEntityID():
            if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
                self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
                DEBUG_MSG("setAttr(canMove, False)")
                self.otherEntity.setAttr("canMove", False)
                self.otherEntity.addSkillControlTimer(
                    "ImprisonCancelTimer",
                    3,
                    0,
                    "self.canMove = True\nDEBUG_MSG('ImprisonCancelTimer scriptString')",
                    "onceOperation")
