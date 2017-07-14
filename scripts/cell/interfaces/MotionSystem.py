# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class MotionSystem:
    def __init__(self):
        DEBUG_MSG("MotionSystem:__init__")
        self.canMove = True

    def requestMove(self, exposed, point):
        if self.canMove:
            self.allClients.DoMove(point)

    def stopMove(self, exposed):
        # DEBUG_MSG("Avatar:stopMove")
        if self.canMove:
            self.allClients.OnStopMove()
