# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math


class CombatBulletinSystem:
    def __init__(self):
        DEBUG_MSG("CombatBulletinSystem:__init__")
        targethour = datetime.timedelta(hours=21)
        now = datetime.datetime.now()
        nowhour = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        hourdelta = targethour - nowhour
        if hourdelta.days < 0:
            targethour = datetime.timedelta(hours=24, minutes=1, seconds=1)
            hourdelta = targethour - nowhour
            self.addTimer(hourdelta.total_seconds(), 0, 3)
        else:
            self.addTimer(0, 60 * 60, 0)

    def onTimer(self, timerHandle, userData):
        if userData == 0:
            DEBUG_MSG("hourTimer")
            lefthours, leftminutes, leftseconds = self.calculateHMS(self.getTotalSeconds())
            self.publishBulletin("距离开战还有" + str(lefthours) + "小时" + str(leftminutes) + "分钟" + str(leftseconds) + "秒")
            if lefthours < 1:
                self.minuteTimer = self.addTimer(60, 60 * 5, 1)
                self.delTimer(timerHandle)
        elif userData == 1:
            DEBUG_MSG("minuteTimer")
            lefthours, leftminutes, leftseconds = self.calculateHMS(self.getTotalSeconds())
            self.publishBulletin("距离开战还有" + str(lefthours) + "小时" + str(leftminutes) + "分钟" + str(leftseconds) + "秒")
            if leftminutes < 1:
                self.minuteTimer = self.addTimer(0, 1, 2)
                self.delTimer(timerHandle)
        elif userData == 2:
            DEBUG_MSG("secondTimer")
            lefthours, leftminutes, leftseconds = self.calculateHMS(self.getTotalSeconds())
            self.publishBulletin("距离开战还有" + str(lefthours) + "小时" + str(leftminutes) + "分钟" + str(leftseconds) + "秒")
            if leftseconds <= 1:
                DEBUG_MSG("Start Resource War")
                KBEngine.globalData["space_cell_MuLingCunSpace"].closeShield()
                self.addTmer(4, 3 * 3600 + 2, 4)
                self.delTimer(timerHandle)
        elif userData == 3:
            DEBUG_MSG("nextHourTimer")
            self.hourTimerHandle = self.addTimer(0, 60 * 60, 0)
            self.delTimer(timerHandle)
        elif userData == 4:
            DEBUG_MSG("Restart Combat Bulletin Timer")
            targethour = datetime.timedelta(hours=21)
            now = datetime.datetime.now()
            nowhour = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
            hourdelta = targethour - nowhour
            if hourdelta.days < 0:
                targethour = datetime.timedelta(hours=24, minutes=1, seconds=1)
                hourdelta = targethour - nowhour
                self.addTimer(hourdelta.total_seconds(), 0, 3)
            else:
                self.addTimer(0, 60 * 60, 0)
            self.delTimer(timerHandle)

    def getTotalSeconds(self):
        targethour = datetime.timedelta(hours=21)
        now = datetime.datetime.now()
        nowhour = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        hourdelta = targethour - nowhour
        return hourdelta.total_seconds()

    def calculateHours(self, total_seconds):
        return int(math.floor(float(total_seconds) / 3600))

    def calculateMinutes(self, total_seconds, lefthours):
        return int((float(total_seconds) - lefthours * 3600) / 60)

    def calculateSeconds(self, total_seconds, lefthours, leftminutes):
        return int(float(total_seconds) - lefthours * 3600 - leftminutes * 60)

    def calculateHMS(self, total_seconds):
        lefthours = self.calculateHours(total_seconds)
        leftminutes = self.calculateMinutes(total_seconds, lefthours)
        leftseconds = self.calculateSeconds(total_seconds, lefthours, leftminutes)
        return lefthours, leftminutes, leftseconds
