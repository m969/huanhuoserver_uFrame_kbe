# -*- coding: utf-8 -*-
from triggerStrategies.TriggerStrategy import *
from Skills import *


class SkillSystem:
    def __init__(self):
        self.canCastSkill = True

    def requestCastSkill(self, exposed, skillName, argsString):
        if exposed != self.id:
            return
        exec("self.skill = " + skillName + "(self, argsString)")
        self.skill.cast()
