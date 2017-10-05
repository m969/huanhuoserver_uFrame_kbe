# -*- coding: utf-8 -*-
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject


class Trigger(KBEngine.Entity, EntityObject):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        # DEBUG_MSG("Trigger:__init__")
        # DEBUG_MSG(self.triggerStrategy)
        self.isTrigger = True
        if self.lifeSpans > 0:
            self.addTimer(self.lifeSpans, 0, 0)
        if self.circleTrigger is True:
            # DEBUG_MSG("circleTrigger is True")
            self.entityList = {}
            self.delEntityList = []
            self.addTimer(0, 0.1, 1)

        DEBUG_MSG("entityName = " + str(self.entityName))

    def onTimer(self, tid, userArg):
        if userArg == 0:
            self.destroy()
        elif userArg == 1:
            for entityId, entityInfo in self.entityList.items():
                entity = entityInfo["entity"]
                hasEntered = entityInfo["hasEntered"]
                if entity is not None:
                    dist = self.position.distTo(entity.getAttr("position"))
                    if dist < self.triggerSize:
                        if hasEntered is False:
                            entityInfo["hasEntered"] = True
                            if self.triggerStrategy.__class__.__name__ is "dict":
                                for strategy in self.triggerStrategy.values():
                                    strategy.setInfo(self, entity, self.triggerSize, self.triggerSize,
                                                     self.triggerControllerID, userArg)
                                    strategy.execute()
                            if self.triggerStrategy.__class__.__name__ is not "dict":
                                self.triggerStrategy.setInfo(self, entity, self.triggerSize, self.triggerSize,
                                                 self.triggerControllerID, userArg)
                                self.triggerStrategy.execute()
                    else:
                        if hasEntered is True:
                            entityInfo["hasEntered"] = False
                else:
                    DEBUG_MSG("entity is None")
            tempDelEntityList = self.delEntityList.copy()
            for entityId in tempDelEntityList:
                if entityId in self.entityList:
                    del self.entityList[entityId]
                    self.delEntityList.remove(entityId)

    def onEnterTrap(self, other, rangeXZ, rangeY, controllerID, userArg):
        """
        当进入触发器时
        """
        if self.circleTrigger is True:
            if other.getAttr("id") == self.owner.getAttr("id"):
                return
            if self.entityList.get(other.getAttr("id"), None) is not None:
                return
            self.entityList[other.getAttr("id")] = {"entity": other, "hasEntered": False}
            self.triggerControllerID = controllerID
        else:
            if self.triggerStrategy.__class__.__name__ == "dict":
                for strategy in self.triggerStrategy.values():
                    strategy.setInfo(self, other, rangeXZ, rangeY, controllerID, userArg)
                    strategy.execute()
            # DEBUG_MSG("class name " + self.triggerStrategy.__class__.__name__)
            if self.triggerStrategy.__class__.__name__ != "dict":
                self.triggerStrategy.setInfo(self, other, rangeXZ, rangeY, controllerID, userArg)
                self.triggerStrategy.execute()

    def onLeaveTrap(self, other, rangeXZ, rangeY, controllerID, userArg):
        """
        当离开触发器时
        """
        if self.circleTrigger is True:
            if self.entityList.get(other.getAttr("id"), None) is None:
                return
            self.delEntityList.append(other.getAttr("id"))

    def onWitnessed(self, isWitnessed):
        """
        当被看到时
        """
        # DEBUG_MSG("Trigger:onWitnessed")
        self.proximityID = self.addProximity(self.triggerSize, self.triggerSize, 0)

    def moveToPointSample(self, destination, velocity, distance=0.2):
        """
        移动到某点
        """
        self.moveToPoint(destination, velocity, distance, {}, True, True)

    def moveToEntitySample(self, destEntityID, velocity, distance=0.1):
        """
        移动到某点
        """
        self.moveToEntity(destEntityID, velocity, distance, {}, True, True)
