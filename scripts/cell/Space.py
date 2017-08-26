# -*- coding: utf-8 -*-
import space_data
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Space.GateWaySystem import GateWaySystem
from interfaces.Space.MonsterSystem import MonsterSystem
from interfaces.Space.NpcSystem import NpcSystem
from interfaces.Space.ResourceWarSystem import ResourceWarSystem


class Space(KBEngine.Entity, EntityObject, MonsterSystem, NpcSystem, ResourceWarSystem, GateWaySystem):
    """
    游戏场景，在这里代表野外大地图
    """
    def __init__(self):
        DEBUG_MSG("Space:cell:__init__ " + str(self.spaceID) + " " + str(self.id) + " " + self.spaceName)
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        MonsterSystem.__init__(self)
        NpcSystem.__init__(self)
        ResourceWarSystem.__init__(self)
        GateWaySystem.__init__(self)

        KBEngine.globalData["space_%i" % self.spaceID] = self.base
        KBEngine.globalData["space_" + self.spaceName] = self.base
        KBEngine.globalData["space_cell_%i" % self.spaceID] = self
        KBEngine.globalData["space_cell_" + self.spaceName] = self

        self.spaceData = space_data.data[self.cityName]     # 取出自身的场景数据
        self.respawnPoint = self.spaceData["重生点"]

    def onDestroy(self):
        """
        KBEngine method.
        """
        del KBEngine.globalData["space_%i" % self.spaceID]
        del KBEngine.globalData["space_" + self.spaceName]
        del KBEngine.globalData["space_cell_%i" % self.spaceID]
        del KBEngine.globalData["space_cell_" + self.spaceName]
        self.destroySpace()

    def onEnter(self, entityMailbox):
        """
        defined method.
        进入场景
        """
        DEBUG_MSG('Space::onEnter space[%d] entityID = %i.' % (self.spaceID, entityMailbox.id))
        entityMailbox.cell.onAvatarEnterSpace(self.spaceID, space_data.data[self.cityName]["场景名称"])

    def onTimer(self, timerHandle, userData):
        MonsterSystem.onTimer(self, timerHandle, userData)

    def onLeave(self, entityID):
        """
        defined method.
        离开场景
        """
        DEBUG_MSG('Space::onLeave space entityID = %i.' % (entityID))
