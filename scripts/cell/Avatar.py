# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Avatar.ChatChannelSystem import ChatChannelSystem
from interfaces.Avatar.CampSystem import CampSystem
from interfaces.Avatar.DialogSystem import DialogSystem
from interfaces.EntityObject import EntityObject
from interfaces.Avatar.FriendSystem import FriendSystem
from interfaces.HealthSystem import HealthSystem
from interfaces.Avatar.MotionSystem import MotionSystem
from interfaces.Avatar.SkillSystem import SkillSystem
from interfaces.Avatar.SuperPowerSystem import SuperPowerSystem
from interfaces.Avatar.TeleportSystem import TeleportSystem


class AvatarState:
    def __init__(self):
        DEBUG_MSG("AvatarState")


class StandState(AvatarState):
    def __init__(self):
        DEBUG_MSG("StandState")
        AvatarState.__init__(self)


class RunState(AvatarState):
    def __init__(self):
        DEBUG_MSG("RunState")
        AvatarState.__init__(self)


class Avatar(KBEngine.Entity,
             EntityObject,
             HealthSystem,
             SuperPowerSystem,
             MotionSystem,
             SkillSystem,
             DialogSystem,
             TeleportSystem,
             FriendSystem,
             ChatChannelSystem,
             CampSystem):
    def __init__(self):
        DEBUG_MSG("Avatar.cell:__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        HealthSystem.__init__(self)
        SuperPowerSystem.__init__(self)
        MotionSystem.__init__(self)
        SkillSystem.__init__(self)
        DialogSystem.__init__(self)
        TeleportSystem.__init__(self)
        FriendSystem.__init__(self)
        ChatChannelSystem.__init__(self)
        CampSystem.__init__(self)

    def onTimer(self, timerHandle, userData):
        SuperPowerSystem.onTimer(self, timerHandle, userData)   # 10
        HealthSystem.onTimer(self, timerHandle, userData)       # 20
        DialogSystem.onTimer(self, timerHandle, userData)       # 30
        TeleportSystem.onTimer(self, timerHandle, userData)     # 40

    def setAvatarName(self, entityName):
        self.entityName = entityName

    def onDestroy(self):
        DEBUG_MSG("Avatar:onCellDestroy")
