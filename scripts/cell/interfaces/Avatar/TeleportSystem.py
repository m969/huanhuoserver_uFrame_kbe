# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class TeleportSystem:
    def __init__(self):
        DEBUG_MSG("TeleportSystem:__init__")
        self.counter = 0  # 新场景重置坐标次数计数器

    def onTimer(self, timerHandle, userData):
        if userData == 41:  # 进入新场景重置坐标定时器
            DEBUG_MSG("TeleportSystem : reset position!")
            self.position = self.newSpacePosition
            self.counter += 1
            if self.counter >= 10:
                self.delTimer(timerHandle)

    def isGoingToTeleport(self, spaceName, gateWayEntrancePosition):
        DEBUG_MSG("TeleportSystem:isGoingToTeleport")
        self.client.onMainAvatarLeaveSpace()
        self.newSpaceName = spaceName
        self.newSpacePosition = gateWayEntrancePosition
        pass

    def teleportToSpace(self, spaceCellMailbox, position, direction):
        """
        defined.
        baseapp返回teleportSpace的回调
        """
        DEBUG_MSG("TeleportSystem:teleportToSpace")
        self.getCurrSpaceBase().onLeave(self.id)
        self.teleport(spaceCellMailbox, position, direction)
        self.base.onTeleportSuccess(self.newSpaceName)
        self.counter = 0
        self.resetPositionTimerHandle = self.addTimer(0.1, 0.2, 41)  # 重置角色坐标计数器
        self.onAvatarEnterSpace(spaceCellMailbox.getAttr("spaceID"), spaceCellMailbox.getAttr("spaceName"))

    def _onTeleportSuccess(self, nearbyEntity):
        DEBUG_MSG("TeleportSystem:onTeleportSuccess")
        self.base.onTeleportSuccess(self.newSpaceName)
        self.teleport(None, self.newSpacePosition, (0.0, 0.0, 0.0))

    def onLeaveSpaceClientInputInValid(self, exposed):
        DEBUG_MSG("TeleportSystem:onLeaveSpaceClientInputInValid")
        KBEngine.globalData["space_" + self.newSpaceName].requestTeleport(self.base)
        pass

    def onAvatarEnterSpace(self, spaceID, spaceName):
        DEBUG_MSG("TeleportSystem:onEnterSpace")
        self.client.onMainAvatarEnterSpace(spaceID, spaceName)
        pass
