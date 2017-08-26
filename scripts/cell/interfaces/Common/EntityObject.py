# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class EntityObject:
    def __init__(self):
        # DEBUG_MSG("EntityObject:__init__")
        pass

    def hasAttr(self, attr):
        # DEBUG_MSG("hasAttr : " + attr)
        return hasattr(self, attr)

    def getAttr(self, attr):
        # DEBUG_MSG("getAttr : " + attr)
        return getattr(self, attr, None)

    def setAttr(self, attr, value):
        # exec("DEBUG_MSG(self."+attr+")")
        if hasattr(self, attr):
            setattr(self, attr, value)
        else:
            exec("self." + attr + "= value")
        DEBUG_MSG("setAttr:" + attr + "=" + str(value))

    def delAttr(self, attr):
        DEBUG_MSG("delAttr : " + attr)
        return delattr(self, attr)

    def destroyEntity(self):
        self.destroy()

    def getEntityID(self):
        return self.id

    def getDatabaseID(self):
        return self.base.getDatabaseID()

    def getScriptName(self):
        return self.__class__.__name__

    def getCurrentSpaceBase(self):
        """
        获得当前space的entity baseMailbox
        """
        return KBEngine.globalData["space_%i" % self.spaceID]

    def getCurrentSpace(self):
        """
        获得当前space的entity
        """
        spaceBase = self.getCurrentSpaceBase()
        return KBEngine.entities.get(spaceBase.id, None)
