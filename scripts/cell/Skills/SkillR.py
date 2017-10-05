# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import trigger_strategy
from Skills import *
from triggerStrategies import *


class SkillR(Skill):
    def __init__(self, spellCaster, argsString):
        Skill.__init__(self, spellCaster, argsString)
        args = argsString.split()
        self.enemyId = int(args[0])

    def cast(self):
        damage = int(self.skillSpAmount * self.skillQuality)
        self.strategyData = {"伤害": damage}

        super().cast()

        trigger = KBEngine.createEntity("Trigger",
                                        self.spellCaster.spaceID,
                                        self.spellCaster.position,
                                        self.spellCaster.direction,
                                        {
                                            'entityName': "SkillR_Trigger",
                                            'owner': self.spellCaster,
                                            "campName": self.spellCaster.getAttr("campName"),
                                            'triggerID': 2,
                                            'triggerSize': 4,
                                            'triggerStrategy': self.triggerStrategy
                                        })
        trigger.moveToEntitySample(self.enemyId, 20)
