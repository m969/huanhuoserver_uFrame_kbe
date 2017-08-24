# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class ChatChannelSystem:
    def __init__(self):
        DEBUG_MSG("ChatChannelSystem:__init__")

    def sendChatMessage(self, exposed, selfName, chatContent):
        """
        :param chatContent: 聊天内容
        :return: null
        """
        DEBUG_MSG("ChatChannelSystem:onSendChatMessage" + chatContent)
        self.allClients.ReciveChatMessage(selfName, chatContent)

    def sendVoiceSample(self, exposed, data, length, packetId):
        DEBUG_MSG("ChatChannelSystem:sendVoiceSample")
        self.otherClients.ReciveVoiceSample(data, length, packetId)
