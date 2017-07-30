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
        self.addTimer(1, 3, 12)  # 添加 灵力值恢复 定时器
        self.addTimer(1, 0.5, 13)  # 添加 瞬时释放灵力值恢复 定时器

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
        if userData == 13:  # 瞬时释放灵力值恢复 定时器，每2秒调用一次
            if self.canRevertSP:
                if self.SP >= self.mspRevertStrength:
                    if self.MSP < self.MSP_Max:
                        self.MSP += self.mspRevertStrength
                        self.SP -= self.mspRevertStrength
                        if self.MSP > self.MSP_Max:
                            self.SP += self.MSP - self.MSP_Max
                            self.MSP = self.MSP_Max
                else:
                    self.MSP += self.SP
                    self.SP = 0
