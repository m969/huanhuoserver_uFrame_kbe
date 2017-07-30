# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
from Skills import *
from triggerStrategies import *


class SkillQ(Skill):
    def __init__(self, spellCaster, argsString):
        Skill.__init__(self, spellCaster, argsString)
        args = argsString.split()
        self.skillPoint = (float(args[0]), float(args[1]), float(args[2]))
        self.skillData = avatar_skill_data.data[1]      # 技能1
        self.skillMinSp = self.skillData["levelSpLimit"][1]  # 使用这个技能最少需要的灵力值
        self.skillMaxSp = self.skillData["levelSpLimit"][1]  # 使用这个技能最多可以使用的灵力值

    def cast(self):
        if self.skillPoint is not None:
            skillSpAmount = 0  # 此次技能实际使用的灵力值
            if self.spellCaster.MSP < self.skillMinSp:
                return
            if self.spellCaster.MSP >= self.skillMaxSp:
                skillSpAmount = self.skillMaxSp
                self.spellCaster.MSP -= self.skillMaxSp
            else:
                skillSpAmount = self.spellCaster.MSP
                self.spellCaster.MSP = 0
            skillQuality = self.skillData["quality"]  # 技能品质，即将灵力转化为攻击力的效率
            damage = int(skillSpAmount * skillQuality)

            triggerStrategy = DamageTriggerStrategy()
            triggerStrategy.setData({"伤害": damage})
            trigger = KBEngine.createEntity("Trigger",
                                            self.spellCaster.spaceID,
                                            self.spellCaster.position,
                                            (0.0, 0.0, 0.0),
                                            {
                                                'entityName': "SkillQ_Trigger",
                                                'owner': self.spellCaster,
                                                "campName": self.spellCaster.getAttr("campName"),
                                                'triggerID': 1,
                                                'triggerSize': 4,
                                                'triggerStrategy': triggerStrategy
                                            })
            trigger.moveToPointSample(self.skillPoint, 80)
