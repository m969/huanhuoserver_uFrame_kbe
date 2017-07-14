# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import level_data
import avatar_skill_data


class SuperPowerSystem:
    def __init__(self):
        DEBUG_MSG("SuperPowerSystem:__init__")
        self.MSP = self.MSP_Max
        self.SP = self.SP_Max
        self.canUseSP = True
        self.canRevertSP = True
        self.canIncreaseSPMax = True

        self.skillPool = avatar_skill_data.data
        self.levelInfoData = level_data.level_info_data
        self.levelName = level_data.level_name_data[self.level]
        self.levelPeriodName = level_data.level_period_name_data[self.levelPeriod]

        self.addTimer(1, 60, 11)  # 添加 灵力上限值增加 定时器
        self.addTimer(1, 2, 12)  # 添加 灵力值恢复 定时器

    def onTimer(self, timerHandle, userData):
        if userData == 11:  # 灵力上限值增加 定时器，每60秒调用一次
            if self.canIncreaseSPMax:
                currentLevelSpLimit = self.levelInfoData[self.level]["等阶灵力需求值"][self.levelPeriod]
                if self.SP_Max >= currentLevelSpLimit:
                    self.SP_Max = currentLevelSpLimit
                else:
                    self.SP_Max += self.spMaxIncreaseStrength  # 历练度
        if userData == 12:  # 灵力值恢复 定时器，每2秒调用一次
            if self.canRevertSP:
                if self.SP >= self.SP_Max:
                    self.SP = self.SP_Max
                else:
                    self.SP += self.spRevertStrength
