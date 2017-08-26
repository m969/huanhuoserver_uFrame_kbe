# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.Strategy import Strategy


class TriggerStrategy(Strategy):
    """
    触发器策略
    """
    def __init__(self):
        Strategy.__init__(self)

    def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
        """
        设置触发器的信息
        """
        self.trigger = trigger
        self.otherEntity = otherEntity
        self.triggerRangeXZ = rangeXZ
        self.triggerRangeY = rangeY
        self.triggerControllerID = controllerID
        self.triggerUserArg = userArg

    def initializeStrategy(self, strategyData):
        pass

    def execute(self):
        """
        触发器策略的执行方法
        """
        Strategy.execute(self)
        if self.otherEntity.getEntityID() == self.trigger.owner.getEntityID():
            return
