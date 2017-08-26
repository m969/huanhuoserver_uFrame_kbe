# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import space_data
from triggerStrategies import *


class GateWaySystem:
    def __init__(self):
        DEBUG_MSG("GateWaySystem:__init__")

        self.spaceData = space_data.data[self.cityName]     # 取出自身的场景数据

        self.triggerData = self.spaceData["触发器数据"]      # 取出场景触发器数据
        for triggerData in self.triggerData.values():
            exec("self.triggerStrategy = " + triggerData["触发器类型"] + "Strategy()")
            DEBUG_MSG(self.triggerStrategy)
            self.triggerStrategy.initializeStrategy(triggerData)
            trigger = KBEngine.createEntity("Trigger",
                                            self.spaceID,
                                            triggerData["触发器坐标"],
                                            (0.0, 0.0, 0.0),
                                            {
                                                'entityName': "GateWayTrigger",
                                                'lifeSpans': 0,
                                                'triggerSize': 4,
                                                "triggerStrategy": self.triggerStrategy
                                            })     # 创建触发器
