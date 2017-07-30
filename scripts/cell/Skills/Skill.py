# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Skill:
    def __init__(self, spellCaster, argsString):
        # DEBUG_MSG(self.__class__.__name__ + ":__init__")
        self.spellCaster = spellCaster

    def cast(self):
        # DEBUG_MSG(self.__class__.__name__ + ":cast")
        pass
