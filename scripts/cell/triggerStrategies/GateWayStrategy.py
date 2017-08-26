# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class GateWayStrategy(TriggerStrategy):
    """
    传送门策略
    """

    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.targetSpaceName = strategyData["目标场景"]
        self.gateWayEntrancePosition = strategyData["传送门入口点"]

    def execute(self):
        super().execute()
        if self.otherEntity.getAttr("isAvatar") is True:
            KBEngine.globalData["spacesManager"].teleportToSpaceByName(
                self.targetSpaceName,
                self.gateWayEntrancePosition,
                self.otherEntity.base)
