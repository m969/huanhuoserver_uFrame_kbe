# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.Strategy import Strategy


class TriggerStrategy(Strategy):
    """
    触发器策略
    """

    def __init__(self):
        Strategy.__init__(self)
        pass

    def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
        """
        设置触发器策略的信息
        """
        self.trigger = trigger
        self.otherEntity = otherEntity
        self.triggerRangeXZ = rangeXZ
        self.triggerRangeY = rangeY
        self.triggerControllerID = controllerID
        self.triggerUserArg = userArg

    def setData(self, strategyData):
        pass

    def execute(self):
        """
        策略的执行方法
        :return:
        """
        Strategy.execute(self)
        pass
#
#
# class DamageTriggerStrategy(TriggerStrategy):
#     """
#     伤害策略
#     """
#
#     def __init__(self):
#         TriggerStrategy.__init__(self)
#         pass
#
#     def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
#         super().setInfo(trigger, otherEntity, rangeXZ, rangeY, controllerID, userArg)
#
#     def setData(self, strategyData):
#         super().setData(strategyData)
#         self.damage = strategyData["攻击力"]
#
#     def excute(self):
#         super().excute()
#         # if self.otherEntity.getAttr("className") == self.trigger.owner.getAttr("className"):
#         #     return
#         if self.otherEntity.getAttr("canDamage") is True:
#             if self.otherEntity.getEntityID() != self.trigger.owner.getEntityID():
#                 if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
#                     self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
#
#
# class OnceDamageTriggerStrategy(TriggerStrategy):
#     """
#     伤害策略
#     """
#
#     def __init__(self):
#         TriggerStrategy.__init__(self)
#         pass
#
#     def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
#         super().setInfo(trigger, otherEntity, rangeXZ, rangeY, controllerID, userArg)
#
#     def setData(self, strategyData):
#         super().setData(strategyData)
#         self.damage = strategyData["攻击力"]
#
#     def excute(self):
#         super().excute()
#         # if self.otherEntity.getAttr("className") == self.trigger.owner.getAttr("className"):
#         #     return
#         if self.otherEntity.getAttr("canDamage") is True:
#             if self.otherEntity.getEntityID() != self.trigger.owner.getEntityID():
#                 if self.otherEntity.getAttr("campName") != self.trigger.owner.getAttr("campName"):
#                     self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
#                     self.trigger.destroy()
#
#
# class GateWayTriggerStrategy(TriggerStrategy):
#     """
#     传送门策略
#     """
#
#     def __init__(self):
#         TriggerStrategy.__init__(self)
#         pass
#
#     def setData(self, strategyData):
#         super().setData(strategyData)
#         self.targetSpaceName = strategyData["目标场景"]
#         self.gateWayEntrancePosition = strategyData["传送门入口点"]
#
#     def setInfo(self, trigger=None, otherEntity=None, rangeXZ=None, rangeY=None, controllerID=None, userArg=None):
#         super().setInfo(trigger, otherEntity, rangeXZ, rangeY, controllerID, userArg)
#
#     def excute(self):
#         super().excute()
#         if self.otherEntity.getAttr("isAvatar") is True:
#             KBEngine.globalData["spacesManager"].teleportToSpaceByName(
#                 self.targetSpaceName,
#                 self.gateWayEntrancePosition,
#                 self.otherEntity.base)
