# -*- coding: utf-8 -*-
import KBEngine
import copy, enum, operator
from KBEDebug import *
from interfaces.EntityObject import EntityObject
from interfaces.HealthSystem import HealthSystem
from interfaces.SuperPowerSystem import SuperPowerSystem
from interfaces.MotionSystem import MotionSystem
from interfaces.SkillSystem import SkillSystem
from interfaces.DialogSystem import DialogSystem
from interfaces.TeleportSystem import TeleportSystem
from interfaces.FriendSystem import FriendSystem
from interfaces.ChatChannelSystem import ChatChannelSystem


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


class Avatar(KBEngine.Entity, EntityObject, HealthSystem, SuperPowerSystem, MotionSystem, SkillSystem, DialogSystem, TeleportSystem, FriendSystem, ChatChannelSystem):
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

    def onTimer(self, timerHandle, userData):
        SuperPowerSystem.onTimer(self, timerHandle, userData)   # 1
        HealthSystem.onTimer(self, timerHandle, userData)       # 2
        DialogSystem.onTimer(self, timerHandle, userData)       # 3
        TeleportSystem.onTimer(self, timerHandle, userData)     # 4

    def setAvatarName(self, entityName):
        self.entityName = entityName

    def onDestroy(self):
        DEBUG_MSG("Avatar:onCellDestroy")
