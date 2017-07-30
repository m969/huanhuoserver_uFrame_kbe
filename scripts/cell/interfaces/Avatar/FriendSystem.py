# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from FRIENDS_INFO import TFriendsInfo


class FriendSystem:
    def __init__(self):
        DEBUG_MSG("FriendSystem:__init__")

    def findFriends(self, exposed):
        """
        #--郑晓飞---返回数据库中的所有注册人员在客户端进行比对，在客户端检测是否有此搜索朋友
        :param exposed:
        :return:
        """
        DEBUG_MSG("FindFriends")
        avatarId = self.id
        KBEngine.globalData["avatarId"] = self.id
        DEBUG_MSG(avatarId)
        KBEngine.executeRawDatabaseCommand("SELECT sm_entityName from tbl_Avatar", _getAllEntityName)

    def addFriends(self, exposed, goldxFriendsName):
        """
        郑晓飞---添加好友，并将此好友写入数据库
        :return:
        """
        DEBUG_MSG("FriendSystem:AddFriends")
        tempFriends = self.avatarFriends
        DEBUG_MSG(tempFriends)
        tempFriends[goldxFriendsName] = goldxFriendsName
        self.avatarFriends = tempFriends
        DEBUG_MSG(self.avatarFriends)
        self.allClients.OnShowAllFriends(self.avatarFriends)

    def deleteFriends(self, exposed, goldxFriendsName):
        """
        郑晓飞---删除好友，同时也删除数据库中的信息
        :return:
        """
        DEBUG_MSG("FriendSystem:DeleteFriends")
        tempFriends = self.avatarFriends
        DEBUG_MSG(tempFriends)
        del tempFriends[goldxFriendsName]
        self.avatarFriends = tempFriends
        DEBUG_MSG(self.avatarFriends)
        self.allClients.OnShowAllFriends(self.avatarFriends)

    def showAllFriends(self, exposed):
        """
        郑晓飞---显示全部好友
        :return:
        """
        DEBUG_MSG("FriendSystem:ShowAllFriends")
        DEBUG_MSG(self.avatarFriends)
        self.allClients.OnShowAllFriends(self.avatarFriends)

    def sendAvatarNameToClient(self, entityNames):
        """
        将所有玩家的名字发给客户端
        :param entityNames: 数据库中所有注册玩家的字符串
        :return:
        """
        DEBUG_MSG("FriendSystem:SendAvatarNameToClient")
        self.allClients.OnFindFriends(entityNames)


def _getAllEntityName(resultCollect, num, errorInfo):
    DEBUG_MSG("_getAllEntityName")
    DEBUG_MSG(resultCollect)
    entityNames = ""
    if errorInfo is None:
        for value in resultCollect:
            entityNames += str(value[0]) + " "
        DEBUG_MSG(KBEngine.globalData["avatarId"])
        KBEngine.entities[KBEngine.globalData["avatarId"]].SendAvatarNameToClient(entityNames)
        DEBUG_MSG("_getAllEntityName" + entityNames)
    else:
        ERROR_MSG("create tbl failed")
