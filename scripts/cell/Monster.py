# -*- coding: utf-8 -*-
import monster_data
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Common.HealthSystem import HealthSystem
from interfaces.Common.SuperPowerSystem import SuperPowerSystem
from interfaces.Common.SkillSystem import SkillSystem
from interfaces.Monster.AI import AI


class Monster(KBEngine.Entity, EntityObject, AI, HealthSystem, SuperPowerSystem, SkillSystem):
    def __init__(self):
        DEBUG_MSG("Monster::__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        AI.__init__(self)
        HealthSystem.__init__(self)
        SuperPowerSystem.__init__(self)
        SkillSystem.__init__(self)

        self.spawnPos = (0, 0, 0)
        self.timerMoveID = self.addTimer(0, 4, 1)
        self.monsterData = monster_data.data[self.name]
        self.modelName = self.monsterData["模型名称"]
        DEBUG_MSG("modelName is " + str(self.modelName))
        self.HP = self.monsterData["生命值"]
        self.HP_Max = self.monsterData["生命值"]
        self.killerTaskCounterVariableName = self.modelName + "_TaskCounter"

    def receiveSpawnPos(self, spawnPos):
        """
        接收BigWorld中的怪物出生点
        """
        #DEBUG_MSG("Monster:receiveSpawnPos")
        self.spawnPos = spawnPos

    def onTimer(self, tid, userArg):
        AI.onTimer(self, tid, userArg)
        HealthSystem.onTimer(self, tid, userArg)
        SuperPowerSystem.onTimer(self, tid, userArg)
        SkillSystem.onTimer(self, tid, userArg)

    def onDie(self, murderer):
        #DEBUG_MSG("Monster:onDie")
        HealthSystem.onDie(self, murderer)
        if murderer.hasAttr(self.killerTaskCounterVariableName) is True:
            murderer.setAttr(self.killerTaskCounterVariableName,
                             murderer.getAttr(self.killerTaskCounterVariableName) + 1)
        else:
            murderer.setAttr(self.killerTaskCounterVariableName, 1)
        if murderer.hasAttr("Pobudeyi_TaskCounter") is True:
            murderer.setAttr("Pobudeyi_TaskCounter",
                             murderer.getAttr("Pobudeyi_TaskCounter") + 1)
        else:
            murderer.setAttr("Pobudeyi_TaskCounter", 1)
        self.delTimer(self.timerMoveID)
        self.destroy()

    def onDestroy(self):
        KBEngine.globalData["space_%i" % self.spaceID].cell.monsterReborn(self.spawnPos, self.name)
