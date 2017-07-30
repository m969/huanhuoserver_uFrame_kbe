# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import monster_data
import space_data
from triggerStrategies import *


class MonsterSystem:
    def __init__(self):
        DEBUG_MSG("MonsterSystem:__init__")
        self.spaceData = space_data.data[self.cityName]  # 取出自身的场景数据
        self.addTimer(0, 2, 0)    # 怪物生成定时器 每2秒生成5个
        self.monsterSpawnCounter = {}
        self.monsterSpawnPositionList = self.spaceData["怪物数据"]       # 怪物出生点列表
        for monsterName, monsterSpawnPositionList in self.monsterSpawnPositionList.items():
            self.monsterSpawnCounter[monsterName] = 0

    def onTimer(self, timerHandle, userData):
        if userData is 0:
            finishCounter = 0
            for (monsterName, spawnPositionList) in self.monsterSpawnPositionList.items():
                tempCounter = 0
                counter = self.monsterSpawnCounter[monsterName]
                for position in spawnPositionList:
                    if counter >= len(spawnPositionList):
                        finishCounter += 1
                        break
                    else:
                        monster = KBEngine.createEntity(
                                                        "Monster",
                                                        self.spaceID,
                                                        spawnPositionList[counter],
                                                        (0.0, 0.0, 0.0),
                                                        {
                                                            'entityName': monsterName,
                                                            'modelName': monster_data.data[monsterName]["模型名称"]
                                                        })      # 创建Monster
                        monster.receiveSpawnPos(spawnPositionList[counter])
                        if tempCounter >= 5:
                            break
                        counter += 1
                        tempCounter += 1
                        self.monsterSpawnCounter[monsterName] = counter
            if finishCounter >= len(self.monsterSpawnPositionList):
                self.delTimer(timerHandle)

    def monsterReborn(self, spawnPos, name):
        """
        重生怪物
        :param monsterMailbox:
        :return:
        """
        DEBUG_MSG("Space:monsterReborn")
        #重生怪物
        monster = KBEngine.createEntity("Monster", self.spaceID, spawnPos, (0.0, 0.0, 0.0),
                                            {
                                                'entityName': name,
                                                'modelName': monster_data.data[name]["模型名称"]
                                            })
        monster.receiveSpawnPos(spawnPos)
