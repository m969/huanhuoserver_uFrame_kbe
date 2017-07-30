# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
from interfaces.EntityObject import EntityObject


class Avatar(KBEngine.Proxy, EntityObject):
    def __init__(self):
        DEBUG_MSG("Avatar:__init__")
        KBEngine.Proxy.__init__(self)
        EntityObject.__init__(self)

    def onEntitiesEnabled(self):
        DEBUG_MSG("Avatar:onEntitiesEnabled:" + self.spaceName)
        KBEngine.globalData["spacesManager"].loginToSpaceByName(self.spaceName, self)
        KBEngine.globalData["spacesManager"].addNewAvatar(self.id, self)

    def createCell(self, space):
        DEBUG_MSG("Avatar:createCell")
        self.createCellEntity(space)

    def setAvatarName(self, accountName):
        if self.cell:
            self.cell.setAvatarName(accountName)
        else:
            self.cellData["entityName"] = accountName

    def onGetCell(self):
        DEBUG_MSG("onGetCell")

    def onLoseCell(self):
        DEBUG_MSG("Avatar:onLoseCell")
        self.destroy()

    def onDestroy(self):
        DEBUG_MSG("Avatar:onDestroy")
        KBEngine.globalData["spacesManager"].delAvatar(self.id)
        if self.accountEntity is not None:
            self.accountEntity.destroyAccount()

    def onClientGetCell(self):
        DEBUG_MSG("Avatar:onClientGetCell")

    def _onAvatarSaved(self, success, avatar):
        self.destroyCellEntity()

    def onClientDeath(self):
        DEBUG_MSG("Avatar:onClientDeath")
        self.writeToDB(self._onAvatarSaved)

    def teleportToSpace(self, baseMailbox):
        DEBUG_MSG("Avatar:teleportToSpace")
        self.teleport(baseMailbox)

    def onTeleportSuccess(self, spaceName):
        DEBUG_MSG("Avatar:onTeleportSuccess")
        self.spaceName = spaceName

    def publishBulletin(self, bulletinContent):
        DEBUG_MSG("Avatar:publishBulletin")
        self.client.OnPublishBulletin(bulletinContent)
