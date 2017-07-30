# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class ResourceWarSystem:
    def __init__(self):
        DEBUG_MSG("ResourceWarSystem:__init__")
        self.createCamp()
        self.createCampTrigger()
        self.startShield()

    def createCamp(self):
        DEBUG_MSG("ResourceWarSystem:createCamp")
        self.blueCamp = KBEngine.createEntity("Camp",
                              self.spaceID,
                              (91.0, 0.0, 237.0),
                              (0.0, 0.0, 0.0),
                              {
                                    "campName": "蓝营"
                              })
        self.redCamp = KBEngine.createEntity("Camp",
                              self.spaceID,
                              (393.0, 0.0, 242.0),
                              (0.0, 0.0, 0.0),
                              {
                                    "campName": "红营"
                              })

    def createCampTrigger(self):
        DEBUG_MSG("ResourceWarSystem:createCampTrigger")
        self.blueCamp.createCampTrigger()
        self.redCamp.createCampTrigger()

    def startShield(self):
        DEBUG_MSG("ResourceWarSystem:startShield")
        self.blueCamp.startShield()
        self.redCamp.startShield()

    def closeShield(self):
        DEBUG_MSG("ResourceWarSystem:closeShield")
        self.blueCamp.closeShield()
        self.redCamp.closeShield()
