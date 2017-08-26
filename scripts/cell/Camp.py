# -*- coding: utf-8 -*-
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from triggerStrategies import *


class Camp(KBEngine.Entity, EntityObject):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        DEBUG_MSG("Camp:__init__")
        self.campTrigger = None

    def createCampTrigger(self):
        DEBUG_MSG("Camp:createCampTrigger")
        self.triggerStrategy = CampStrategy()
        self.triggerStrategy.initializeStrategy({"伤害": 200})
        if self.campTrigger is None:
            self.campTrigger = KBEngine.createEntity("Trigger",
                                                     self.spaceID,
                                                     self.position,
                                                     (0.0, 0.0, 0.0),
                                                     {
                                                         "entityName": "CampTrigger",
                                                         "owner": self,
                                                         "campName": self.campName,
                                                         "lifeSpans": 0,
                                                         "triggerSize": 50,
                                                         "triggerStrategy": self.triggerStrategy,
                                                         "circleTrigger": True
                                                     })  # 创建阵营触发器
        else:
            self.campTrigger.setAttr("position", self.position)

    def startShield(self):
        DEBUG_MSG("Camp:startShield")

    def closeShield(self):
        DEBUG_MSG("Camp:closeShield")
