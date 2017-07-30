# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from interfaces.CombatBulletinSystem import CombatBulletinSystem

class SpacesManager(KBEngine.Base, CombatBulletinSystem):
    def __init__(self):
        DEBUG_MSG("SpacesManager:__init__")
        KBEngine.Base.__init__(self)
        CombatBulletinSystem.__init__(self)

        KBEngine.globalData["spacesManager"] = self
        # 根据场景配置表（space_data）来创建场景
        KBEngine.globalData["allAvatarBases"] = {}
        for (cityName, spaceData) in space_data.data.items():
            DEBUG_MSG("spaceName:" + spaceData["场景名称"])
            spaceBase = KBEngine.createBaseLocally("Space",
                                               {
                                                   "cityName": cityName,
                                                   "spaceName": spaceData["场景名称"]
                                               })

    def onTimer(self, timerHandle, userData):
        CombatBulletinSystem.onTimer(self, timerHandle, userData)

    def addNewAvatar(self, id, avatar):
        DEBUG_MSG("SpacesManager:addNewAvatar")
        KBEngine.globalData["allAvatarBases"][id] = avatar

    def delAvatar(self, id):
        DEBUG_MSG("SpacesManager:delAvatar")
        del KBEngine.globalData["allAvatarBases"][id]

    def loginToSpaceByName(self, spaceName, entityMailbox):
        """
        通过Space名称登录到Space
        :param spaceName:
        :param entityMailbox:
        :return:
        """
        DEBUG_MSG("SpacesManager:loginToSpaceByName")
        KBEngine.globalData["space_" + spaceName].loginSpace(entityMailbox)

    def teleportToSpaceByName(self, spaceName, gateWayEntrancePosition, entityMailbox):
        """
        通过Space名称传送到Space
        :param spaceName:
        :param entityMailbox:
        :return:
        """
        DEBUG_MSG("SpacesManager:teleportToSpaceByName")
        entityMailbox.cell.isGoingToTeleport(spaceName, gateWayEntrancePosition)

    def logoutSpace(self, avatarID, spaceID):
        """
        defined method.
        某个玩家请求登出这个space
        """
        space = KBEngine.globalData["space_%i" % spaceID]
        space.logoutSpace(avatarID)

    def publishBulletin(self, bulletinContent):
        DEBUG_MSG("SpacesManager:publishBulletin")
        for avatar in KBEngine.globalData["allAvatarBases"].values():
            avatar.publishBulletin(bulletinContent)
