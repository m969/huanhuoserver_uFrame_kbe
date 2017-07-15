# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import npc_data
import goods_data
import level_data
from TASK_INFO import TTaskInfo
from AVATAR_BAG import TAvatarBag
from taskScripts.MuJingGuaiRenWu import MuJingGuaiRenWu
from taskScripts.YanShiLingGuaiRenWu import YanShiLingGuaiRenWu
from taskScripts.Duihuarenwu import Duihuarenwu
from taskScripts.Xiaoshiniudao_San import Xiaoshiniudao_San
from taskScripts.Caijizuanshi import Caijizuanshi
from taskScripts.TanxianshandongRenWu import TanxianshandongRenWu
from taskScripts.Bangzhushenmiren import Bangzhushenmiren
from taskScripts.Sidingzhongsheng import Sidingzhongsheng
from taskScripts.Qianlisongqing import Qianlisongqing
from taskScripts.Xunzhaobaoma import Xunzhaobaoma
from taskScripts.Pobudeyi import Pobudeyi


class DialogSystem:
    def __init__(self):
        DEBUG_MSG("DialogSystem:__init__")
        self.canDialog = True
        self.taskScriptList = {}
        self.finishTaskScriptList = []
        """
        在角色初始化时，遍历角色的任务列表，通过任务的所属npc（avatarTaskInfo[0]）以及任务索引（avatarTaskInfo[1]）
        找出任务的所有信息，
        提取任务脚本信息并且创建任务监视脚本。onTimer函数会每秒调用任务监视脚本的检测函数检测任务是否满足完成条件。
        """
        for (key, avatarTaskInfo) in self.taskInfoList.items():
            npcTaskList = npc_data.data[avatarTaskInfo[0]]
            for (taskIndex, taskInfo) in npcTaskList.items():
                if taskIndex == avatarTaskInfo[1]:
                    taskScript = taskInfo["任务脚本"]
                    nextTaskScriptKey = 0
                    for taskScriptKey in self.taskScriptList.keys():
                        if taskScriptKey >= nextTaskScriptKey:
                            nextTaskScriptKey = taskScriptKey
                    nextTaskScriptKey += 1
                    exec("self.taskScriptList[" + str(nextTaskScriptKey) + "] = " + taskScript + "(self, " + str(
                        nextTaskScriptKey) +
                         ", avatarTaskInfo[0], avatarTaskInfo[1])")
        self.addTimer(1, 1, 31)  # 添加 任务监视检测 定时器

    def onTimer(self, timerHandle, userData):
        if userData == 31:  # 任务监视检测 定时器
            """
            此Timer会每秒调用任务监视脚本的检测函数检测任务是否满足完成条件。
            """
            tempDict = {}
            for k in self.taskScriptList.keys():
                self.taskScriptList[k].detectTaskCompleteness()
            count = 0
            for (key, value) in self.taskScriptList.items():
                for k in self.finishTaskScriptList:
                    if k == key:
                        count = 1
                if count == 0:
                    tempDict[key] = value
            self.taskScriptList = tempDict
            self.finishTaskScriptList.clear()

    def requestBuyGoods(self, exposed, spaceID, npcName, goodsID):
        if exposed != self.id:
            return
        DEBUG_MSG("DialogSystem:requestBuyGoods")
        npcMailbox = KBEngine.globalData["space_cell_%i" % spaceID].requestNpc(npcName)
        result = npcMailbox.requestBuyGoods(self, goodsID)
        self.client.BuyResult(result)
        pass

    def giveGoods(self, goodsID):
        DEBUG_MSG("DialogSystem:giveGoods")
        tempBag = self.avatarBag
        DEBUG_MSG(tempBag)
        tempBag[goodsID] = goodsID
        self.avatarBag = tempBag
        DEBUG_MSG(self.avatarBag)
        # 郑晓飞--小试牛刀三任务--购买木剑
        if goods_data.data[goodsID]['name'] == "木剑":
            if self.hasAttr("Xiaoshiniudao_San_TaskCounter") is True:
                self.setAttr("Xiaoshiniudao_San_TaskCounter",
                             self.getAttr("Xiaoshiniudao_San_TaskCounter") + 1)
            else:
                self.setAttr("Xiaoshiniudao_San_TaskCounter", 1)
        # 郑晓飞--探险山洞任务--获得宝箱
        if goods_data.data[goodsID]['name'] == "精致宝箱":
            if self.hasAttr("TanxianshandongRenWu_TaskCounter") is True:
                self.setAttr("TanxianshandongRenWu_TaskCounter",
                             self.getAttr("TanxianshandongRenWu_TaskCounter") + 1)
            else:
                self.setAttr("TanxianshandongRenWu_TaskCounter", 1)
        # 郑晓飞--采集钻石任务--采集钻石
        if goods_data.data[goodsID]['name'] == "钻石":
            if self.hasAttr("Caijizuanshi_TaskCounter") is True:
                self.setAttr("Caijizuanshi_TaskCounter",
                             self.getAttr("Caijizuanshi_TaskCounter") + 1)
            else:
                self.setAttr("Caijizuanshi_TaskCounter", 1)
        # 郑晓飞--寻找宝马任务--寻找宝马
        if goods_data.data[goodsID]['name'] == "宝马":
            if self.hasAttr("Xunzhaobaoma_TaskCounter") is True:
                self.setAttr("Xunzhaobaoma_TaskCounter",
                             self.getAttr("Xunzhaobaoma_TaskCounter") + 1)
            else:
                self.setAttr("Xunzhaobaoma_TaskCounter", 1)
        # /郑晓飞
        pass

    def deleteGoods(self, goodsID):
        """
        郑晓飞----删除背包中的物品
        :param goodID: 物品ID
        :return:
        """
        DEBUG_MSG("DialogSystem:deleteGoods")
        tempBag = self.avatarBag
        DEBUG_MSG(tempBag)
        if goodsID in tempBag.keys():
            del tempBag[goodsID]
        self.avatarBag = tempBag
        DEBUG_MSG(self.avatarBag)
        # 郑晓飞--千里送情任务--将信给予刘公子(丢弃)
        if goods_data.data[goodsID]['name'] == "信":
            if self.hasAttr("Qianlisongqing_TaskCounter") is True:
                self.setAttr("Qianlisongqing_TaskCounter",
                             self.getAttr("Qianlisongqing_TaskCounter") + 1)
            else:
                self.setAttr("Qianlisongqing_TaskCounter", 1)
        pass

    def deductMoney(self, num):
        DEBUG_MSG("getMoney")
        self.goldCount -= num
        pass

    def requestDialog(self, exposed, spaceID, npcName):
        """
        此函数由客户端调用，此函数会向指定npc请求返回对话的内容。
        """
        if exposed != self.id:
            return
        npcMailbox = KBEngine.globalData["space_cell_%i" % self.spaceID].requestNpc(npcName)
        if npcMailbox:
            dialog = npcMailbox.requestTask(self)
            self.client.DoDialog(npcMailbox.getAttr("name"), dialog)
        else:
            DEBUG_MSG("npcMailbox is None")

    def getTaskInfo(self, npcName):
        DEBUG_MSG("DialogSystem:getTaskInfo")
        specificNpcTaskInfo = []
        for aTaskInfo in self.taskInfoList.values():
            if aTaskInfo[0] == npcName:
                specificNpcTaskInfo.append(aTaskInfo)
        return specificNpcTaskInfo

    def setTaskFinish(self, npcName, taskIndex, watcherIndex):
        """
        任务完成度监视脚本会监测任务是否已完成，如果任务完成了就会调用这个函数，设置角色任务信息为已完成状态，
        并且删除任务完成度监视脚本。
        :param npcName:
        :param taskIndex:
        :return:
        """
        DEBUG_MSG("DialogSystem:setTaskFinish")
        for (key, taskInfo) in self.taskInfoList.items():
            if npcName == taskInfo[0] and taskIndex == taskInfo[1]:
                DEBUG_MSG("setTaskFinish")
                taskInfo[2] = True
                self.taskInfoList[key] = taskInfo
                self.finishTaskScriptList.append(watcherIndex)

    def isTaskFinish(self, npcName, taskIndex):
        DEBUG_MSG("DialogSystem:isTaskFinish")
        for taskInfo in self.taskInfoList.values():
            if npcName == taskInfo[0] and taskIndex == taskInfo[1]:
                DEBUG_MSG("return isTaskFinish")
                return taskInfo[2]
        return False

    def giveAward(self, npcName, taskIndex):
        """
        任务完成给予奖励，由npc调用，成功给予奖励后设置角色任务信息为已提交。
        :param npcName:
        :param taskIndex:
        :return:
        """
        DEBUG_MSG("DialogSystem:giveAward")
        self.goldCount += npc_data.data[npcName][taskIndex]["金币奖励"]
        for (propName, propCount) in npc_data.data[npcName][taskIndex]["道具奖励"].items():
            # goodsInfo = {0:propName, 1:propCount}
            i = 0
            for (k, va) in goods_data.data.items():
                if propName == va["name"]:
                    i = 1
                    DEBUG_MSG("give prop id = " + str(k))
                    self.giveGoods(k)
            if i == 0:
                DEBUG_MSG("has no this prop!")
        # 郑晓飞------丢掉任务道具
        for (propName, propCount) in npc_data.data[npcName][taskIndex]["道具丢弃"].items():
            i = 0
            for (k, va) in goods_data.data.items():
                if propName == va["name"]:
                    i = 1
                    DEBUG_MSG("delete prop id = " + str(k))
                    self.deleteGoods(k)
            if i == 0:
                DEBUG_MSG("has no this prop!")
        # 郑晓飞
        for (key, value) in self.taskInfoList.items():
            if value[0] == npcName and value[1] == taskIndex:
                self.taskInfoList[key][3] = True
                return

    def giveTask(self, npcName, taskIndex):
        """
        赋予任务，由npc调用。
        :param npcName:
        :param taskIndex:
        :return:
        """
        DEBUG_MSG("DialogSystem:giveTask")
        taskInfo = TTaskInfo()
        taskInfo.extend([npcName, taskIndex, False, False])
        self.taskInfoList[npcName + str(taskIndex)] = taskInfo
        taskScript = npc_data.data[npcName][taskIndex]["任务脚本"]
        indexOnAvatarTaskScriptList = 0
        for keyIndex in self.taskScriptList.keys():
            DEBUG_MSG("taskScriptList.keys() = ")
            DEBUG_MSG(self.taskScriptList.keys())
            if keyIndex >= indexOnAvatarTaskScriptList:
                indexOnAvatarTaskScriptList = keyIndex
        indexOnAvatarTaskScriptList += 1
        exec("self.taskScriptList[" + str(indexOnAvatarTaskScriptList) + "] = " + taskScript + "(self, " + str(
            indexOnAvatarTaskScriptList) +
             ", npcName, taskIndex)")
