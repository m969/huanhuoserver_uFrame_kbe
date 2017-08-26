# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class SkillTriggerStrategy(TriggerStrategy):
    """
    触发器策略
    """
    def __init__(self):
        super().__init__()

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)

    def execute(self):
        """
        技能触发器策略的执行方法
        """
        super().execute()
