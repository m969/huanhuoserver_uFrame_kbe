# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class MotionSystem:
    def __init__(self):
        DEBUG_MSG("MotionSystem:__init__")
        self.controlledBy = None
        self.movementId = 0
        self.canMove = True

    def requestMove(self, exposed, point):
        self.controlledBy = None
        if self.canMove:
            self.moveToPointSample(point, 20)
            self.allClients.DoMove(point)

    def stopMove(self):
        # DEBUG_MSG("Avatar:stopMove")
        # self.cancelController(self.movementId)
        self.allClients.OnStopMove()

    def moveToPointSample(self, destination, velocity, distance=0.2):
        """
        移动到某点
        """
        self.movementId = self.moveToPoint(destination, velocity, distance, {}, True, True)

    def onMoveOver(self, controllerID, userData):
        self.stopMove()

    def onMove(self, controllerID, userData):
        pass
