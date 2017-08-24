# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import trigger_strategy
from Skills import *
from triggerStrategies import *


class Skill:
    def __init__(self, spellCaster, argsString):
        # DEBUG_MSG(self.__class__.__name__ + ":__init__")
        self.spellCaster = spellCaster
        self.initSkillData()

    def initSkillData(self):
        self.skillData = avatar_skill_data.data[self.__class__.__name__]              # 技能信息
        self.skillMinSp = self.skillData["levelSpLimit"][1]     # 使用这个技能最少需要的灵力值
        self.skillMaxSp = self.skillData["levelSpLimit"][1]     # 使用这个技能最多可以使用的灵力值
        self.skillQuality = self.skillData["quality"]  # 技能品质，即将灵力转化为技能效果的效率

        self.skillSpAmount = 0  # 此次技能实际使用的灵力值
        if self.spellCaster.MSP < self.skillMinSp:
            pass
        else:
            if self.spellCaster.MSP >= self.skillMaxSp:
                self.skillSpAmount = self.skillMaxSp
                self.spellCaster.MSP -= self.skillMaxSp
            else:
                self.skillSpAmount = self.spellCaster.MSP
                self.spellCaster.MSP = 0

    def cast(self):
        # DEBUG_MSG(self.__class__.__name__ + ":cast")
        self.triggerStrategy = {}
        for strategyName in self.skillData["strategies"]:
            exec("self.strategy = " + trigger_strategy.data[strategyName] + "()")
            self.strategy.initializeStrategy(self.strategyData)
            self.triggerStrategy.__setitem__(trigger_strategy.data[strategyName], self.strategy)
