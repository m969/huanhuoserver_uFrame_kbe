# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.EntityObject import EntityObject
import monster_data
import npc_data
import space_data


class Space(KBEngine.Base, EntityObject):
    def __init__(self):
        DEBUG_MSG("Space:__init__")
        KBEngine.Base.__init__(self)
        EntityObject.__init__(self)
        self.spaceName = self.cellData["spaceName"]
        self.spaceData = space_data.data[self.cellData["cityName"]]     # 取出自身的场景数据
        self.createInNewSpace(None)

    def onGetCell(self):
        DEBUG_MSG("Space:onGetCell")

    def loginSpace(self, entityMailbox):
        DEBUG_MSG("Space:loginSpace")
        entityMailbox.createCell(self.cell)
        self.onEnter(entityMailbox)

    def logoutSpace(self, entityID):
        """
        defined method.
        某个玩家请求登出这个space
        """
        self.onLeave(entityID)

    def requestTeleport(self, entityMailbox):
        """
        defined method.
        请求进入某个space中
        """
        DEBUG_MSG("Space:requestTeleport")
        entityMailbox.cell.teleportToSpace(self.cell, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

    def onEnter(self, entityMailbox):
        DEBUG_MSG("Space:onEnter")
        if self.cell is not None:
            self.cell.onEnter(entityMailbox)

    def onLeave(self, entityID):
        """
        defined method.
        离开场景
        """
        if self.cell is not None:
            self.cell.onLeave(entityID)
