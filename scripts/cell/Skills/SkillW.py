# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import trigger_strategy
from Skills import *
from triggerStrategies import *


class SkillW(Skill):
    def __init__(self, spellCaster, argsString):
        Skill.__init__(self, spellCaster, argsString)
        args = argsString.split()
        self.skillPoint = (float(args[0]), float(args[1]), float(args[2]))

    def cast(self):
        damage = int(self.skillSpAmount * self.skillQuality)
        self.strategyData = {"伤害": damage}

        super().cast()

        trigger = KBEngine.createEntity("Trigger",
                                        self.spellCaster.spaceID,
                                        self.skillPoint,
                                        (0.0, 0.0, 0.0),
                                        {
                                            'entityName': "SkillW_Trigger",
                                            'owner': self.spellCaster,
                                            "campName": self.spellCaster.getAttr("campName"),
                                            'triggerID': 2,
                                            'triggerSize': 4,
                                            'triggerStrategy': self.triggerStrategy
                                        })
