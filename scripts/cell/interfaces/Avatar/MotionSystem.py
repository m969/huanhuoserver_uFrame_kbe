# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class MotionSystem:
    def __init__(self):
        DEBUG_MSG("MotionSystem:__init__")
        self.controlledBy = None
        self.canMove = True

    def requestMove(self, exposed, point):
        DEBUG_MSG("MotionSystem:requestMove")
        DEBUG_MSG(self.canMove)
        DEBUG_MSG(self.topSpeed)
        DEBUG_MSG(point)
        if self.canMove:
            self.moveToPointSample(point, 20)
            # self.allClients.DoMove(point)

    def stopMove(self, exposed):
        # DEBUG_MSG("Avatar:stopMove")
        self.allClients.OnStopMove()
