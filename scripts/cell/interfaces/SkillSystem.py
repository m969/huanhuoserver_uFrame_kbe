# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
import avatar_skill_data
import npc_data
import goods_data
import level_data
from triggerStrategies.onEnterTrap.TriggerStrategy import *


class SkillSystem:
    def __init__(self):
        DEBUG_MSG("SkillSystem:__init__")
        self.canSpellSkill = True

    def doSkill(self, *args, **kwargs):
        DEBUG_MSG("Avatar:doSkill", args)

    def requestDoSkillQ(self, exposed, point, yaw):
        if exposed != self.id:
            return
        if point is not None:
            skillData = avatar_skill_data.data[1]  # 技能1
            minSp = skillData["levelSpLimit"][1]  # 使用这个技能最少需要的灵力值
            maxSp = skillData["levelSpLimit"][1]  # 使用这个技能最多可以使用的灵力值
            skillSpAmount = 0  # 此次技能实际使用的灵力值
            if self.MSP < minSp:
                return
            if self.MSP >= maxSp:
                skillSpAmount = maxSp
                self.MSP -= maxSp
            else:
                skillSpAmount = self.MSP
                self.MSP = 0
            skillQuality = skillData["quality"]  # 技能品质，即将灵力转化为攻击力的效率
            damage = int(skillSpAmount * skillQuality)

            triggerStrategy = DamageTriggerStrategy()
            triggerStrategy.setData({"攻击力": damage})
            trigger = KBEngine.createEntity("Trigger",
                                            self.spaceID,
                                            self.position,
                                            (0.0, 0.0, yaw),
                                            {
                                                'entityName': "SkillQ_Trigger",
                                                'owner': self,
                                                'triggerID': 1,
                                                'triggerSize': 4,
                                                'triggerStrategy': triggerStrategy
                                            })
            trigger.moveToPointSample(point, 80)

        self.allClients.DoSkillQ(point, yaw)  # 在客户端上调用DoSkillQ函数

    def requestDoSkillW(self, exposed, point):
        DEBUG_MSG("Avatar:requestDoSkillW")
        if exposed != self.id:
            return
        if point is not None:
            skillData = avatar_skill_data.data[2]  # 技能2
            minSp = skillData["levelSpLimit"][1]  # 使用这个技能最少需要的灵力值
            maxSp = skillData["levelSpLimit"][1]  # 使用这个技能最多可以使用的灵力值
            skillSpAmount = 0  # 此次技能实际使用的灵力值
            if self.MSP < minSp:
                return
            if self.MSP >= maxSp:
                skillSpAmount = maxSp
                self.MSP -= maxSp
            else:
                skillSpAmount = self.MSP
                self.MSP = 0
            skillQuality = skillData["quality"]  # 技能品质，即将灵力转化为攻击力的效率
            damage = int(skillSpAmount * skillQuality)

            triggerStrategy = DamageTriggerStrategy()
            triggerStrategy.setData({"攻击力": damage})
            trigger = KBEngine.createEntity("Trigger",
                                            self.spaceID,
                                            point,
                                            (0.0, 0.0, 0.0),
                                            {
                                                'entityName': "SkillW_Trigger",
                                                'owner': self,
                                                'triggerID': 2,
                                                'triggerSize': 4,
                                                'triggerStrategy': triggerStrategy
                                            })
        self.allClients.DoSkillW(point)
