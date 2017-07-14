# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class ChatChannelSystem:
    def __init__(self):
        DEBUG_MSG("ChatChannelSystem:__init__")

    def onSendChatMessage(self, exposed, selfName, chatContent):
        """
        郑晓飞---响应客户端的聊天函数并将聊天内容转发给其他客户端
        :param chatContent: 聊天内容
        :return: null
        """
        DEBUG_MSG("ChatChannelSystem:onSendChatMessage" + chatContent)
        self.allClients.onReciveChatMessage(selfName, chatContent)
