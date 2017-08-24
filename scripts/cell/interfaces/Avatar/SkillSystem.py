# -*- coding: utf-8 -*-
from triggerStrategies.TriggerStrategy import *
from Skills import *
import avatar_skill_data


class SkillSystem:
    def __init__(self):
        self.canCastSkill = True
        self.nameToTimerIdsDict = {}
        self.timerIdToNameDict = {}
        self.lastUserData = 100

    def requestCastSkill(self, exposed, skillName, argsString):
        if exposed != self.id:
            return
        skillData = avatar_skill_data.data[skillName]              # 技能信息
        skillMinSp = skillData["levelSpLimit"][1]     # 使用这个技能最少需要的灵力值
        if self.MSP < skillMinSp:
            return

        exec("self.skill = " + skillName + "(self, argsString)")
        self.skill.cast()

    def addSkillControlTimer(self, timerType, firstTime, repeatOffset, scriptString, operationType):
        DEBUG_MSG("SkillSystem:addSkillControlTimer")

        if len(self.timerIdToNameDict) == 0:
            self.lastUserData = 100
        timerId = self.addTimer(firstTime, repeatOffset, self.lastUserData + 1)

        self.timerIdToNameDict[timerId] = timerType

        if timerType in self.nameToTimerIdsDict.keys():
            timerIdList = self.nameToTimerIdsDict[timerType]["timerIdList"]
            if timerIdList is not None:
                timerIdList.append(timerId)
                self.nameToTimerIdsDict[timerType]["timerIdList"] = timerIdList
        else:
            self.nameToTimerIdsDict[timerType] = \
                {
                    "timerIdList": [timerId],
                    "scriptString": scriptString,
                    "operationType": operationType
                }

    def onTimer(self, timerHandle, userData):
        # 持续状态效果、瞬时性效果

        if userData > 100:
            timerType = self.timerIdToNameDict[timerHandle]

            exec(self.nameToTimerIdsDict[timerType]["scriptString"])

            timerIdList = self.nameToTimerIdsDict[timerType]["timerIdList"]
            timerIdList.remove(timerHandle)
            if len(timerIdList) == 0:
                del self.nameToTimerIdsDict[timerType]
            else:
                self.nameToTimerIdsDict[timerType]["timerIdList"] = timerIdList

            del self.timerIdToNameDict[timerHandle]
            self.delTimer(timerHandle)
