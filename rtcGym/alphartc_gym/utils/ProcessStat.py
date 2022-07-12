#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import stat_result
import math


class ProcessStat:
    def __init__(self, historyLength: int = 4, PSNRTrueVal_MODE = False):
        self.realPSNR = []
        self.PSNRrecord = []
        self.Delayrecord = []
        self.skipRecord = []
        self.bitRateRecord = []

        self.width = 0      #also works as a start flag
        self.psnrDelta = 0
        self.lastPsnr = 0
        self.historyLength = historyLength
        self.deltaT = 0
        self.skipCount = 0

        self.totalFrame = 0
        self.avgFrameBetween = 0
        self.processCnt = 0
        self.emptyCnt = 0
        self.statePsnr = []
        self.stateDelay = []
        self.stateSkip = []
        self.stateBitrate = []
        self.PSNRTrueVal_MODE = PSNRTrueVal_MODE

    def processStat(self, stat, PSNRI, widthI, DropI, sendI, beforeDecI, isKeyI):   
        #record the frame information
        # only record, failed frames are recorded as -1
        [ [ ["psnr", "w"], ["psnr", "w"], ["psnr", "w"], ["psnr", "w"], ["psnr", "w"] ],[],[],[],[] ]
        #=========================================
        # psnr
        psnrStat = []
        delayStat = []
        skipStat = []
        psnrTmp = []
        delayTmp = []
        skipTmp = []
        bitRateTmp = []

        #if there is key frame in this state
        isKey = False
        for i in stat:
            if i[isKeyI]:
                isKey = True
                break

        if self.width != 0 or stat != []:
            if self.totalFrame == 0:        #at start
                for i in stat:
                    if i[DropI] == 1 or i[DropI] == -3:
                        self.totalFrame += 1
            else:
                self.totalFrame += len(stat)
            self.processCnt += 1
            self.avgFrameBetween = int(self.totalFrame / self.processCnt)
            print("avgFrameBetween: ", self.avgFrameBetween)

        if stat == []:
            print("stat is empty!!!")
            if self.width == 0:     #havent started
                return False, [], [], [], isKey, self.width
            else:   #already started, but no frame recved in the interval
                i = 0
                while i < len(self.PSNRrecord[-1]):
                    j = i
                    while j < len(self.PSNRrecord[-1]):
                        if self.PSNRrecord[-1][j][0] != -1:
                            fakeDelay = self.Delayrecord[-1][j] + 200
                            fakePsnr = self.PSNRrecord[-1][j]
                            break
                        else:
                            j += 1
                    delayTmp.append(fakeDelay)
                    psnrTmp.append(fakePsnr)
                    i += 1

                for j in self.skipRecord[-1]:
                    skipTmp.append(-1)


        else:       #recved frame
            for i in stat:
                if i[DropI] == 1 or i[DropI] == -3:     #this frame is successfully transmitted
                    if self.width == 0:
                        self.width = i[widthI]
                    if self.width != i[widthI]:
                        self.psnrDelta += self.lastPsnr - i[PSNRI]
                        #self.psnrDelta = 0
                        self.width = i[widthI]
                    self.lastPsnr = i[PSNRI]
                    if self.PSNRTrueVal_MODE:
                        psnrTmp.append([math.pow(10, i[PSNRI] / 10000 / 10) / 15848 * 420000 * self.width / 1280, i[widthI]])
                    else:
                        psnrTmp.append([i[PSNRI]* self.width / 1280, i[widthI]])

                    t = i[beforeDecI] - i[sendI]
                    if t < 0:
                        t = i[beforeDecI] - i[sendI] + 1000000
                    delayTmp.append(t)
                    skipTmp.append(1)

                else:
                    if self.width == 0:
                        continue
                    else:
                        psnrTmp.append([-1, -1])

                        delayTmp.append(-1)

                        skipTmp.append(-1)

        self.PSNRrecord.append(psnrTmp)
        self.Delayrecord.append(delayTmp)
        self.skipRecord.append(skipTmp)

        #choose the last Four
        if len(self.PSNRrecord) < self.historyLength:
            startIndex = 0
            endIndex = len(self.PSNRrecord) - 1
        else:
            startIndex = len(self.PSNRrecord) - self.historyLength
            endIndex = len(self.PSNRrecord) - 1



        index = startIndex
        while index <= endIndex:
            psnrGroup = []
            for psnr in self.PSNRrecord[index]:
                psnrGroup.append(psnr[0])
            psnrStat.append(psnrGroup)
            delayStat.append(self.Delayrecord[index])
            skipStat.append(self.skipRecord[index])

            index += 1

        print("psnrStat: ", psnrStat)
        print("delayStat: ", delayStat)
        print("skipStat: ", skipStat)
        return True, psnrStat, delayStat, skipStat, isKey, self.width

    def gotState(self, psnr, delay, skip):
        # generate state
        print("skipCount: ", self.skipCount)
        length = len(psnr)

        sumPsnr = 0
        sumDelay = 0
        sumSkip = 0
        cnt = 0

        index = 0
        #recved frame
        if skip[-1] == 1:
            skipCount = self.skipCount
            while index < length:   # each value
                if skipCount > 0:
                    skipCount -= 1      # extract the counted-skipped frames
                elif psnr[index] != -1:
                    sumPsnr += psnr[index]
                    sumDelay += delay[index]
                    cnt += 1
                index += 1

            index = 0
            sumSkip = 0
            skipCount = self.skipCount
            while index < length:   # each value
                if skipCount > 0:
                    skipCount -= 1      # extract the counted-skipped frames
                else:
                    contiSkip = 0
                    while index < length and skip[index] != 1 :
                        contiSkip += 1
                        index += 1
                    if contiSkip != 0:
                        sumSkip += pow(2, contiSkip - 1)
                index += 1

            if cnt != 0:
                psnrState = float(sumPsnr / cnt)
                delayState = float(sumDelay / cnt)
                if length - self.skipCount < self.avgFrameBetween:
                    sumSkip += pow(2, self.avgFrameBetween - (length - self.skipCount) - 1)
                if sumSkip > pow(2, self.avgFrameBetween - 1):
                    sumSkip = pow(2, self.avgFrameBetween - 1)
                skipState = sumSkip
                self.skipCount = self.avgFrameBetween - (length - self.skipCount)
                if self.skipCount < 0:
                    self.skipCount = 0
            else:
                index = 0
                skipCount = self.skipCount
                while index < length:   # each value
                    if skipCount > 0:
                        skipCount -= 1      # extract the counted-skipped frames
                    if psnr[index] != -1:
                        sumPsnr += psnr[index]
                        sumDelay += delay[index]
                        cnt += 1
                    index += 1
                psnrState = float(sumPsnr / cnt)
                delayState = float(sumDelay / cnt)
                skipState = pow(2, self.avgFrameBetween - 1)
                self.skipCount = skipCount
                self.skipCount += self.avgFrameBetween

        #recv no frame, stat is empty
        else:
            while index < length:   # each value
                sumPsnr += psnr[index]
                sumDelay += delay[index]
                cnt += 1
                index += 1


            sumSkip += pow(2, self.avgFrameBetween - 1)

            psnrState = float(sumPsnr / cnt)
            delayState = float(sumDelay / cnt)
            if sumSkip > pow(2, self.avgFrameBetween - 1):
                sumSkip = pow(2, self.avgFrameBetween - 1)
            skipState = sumSkip
            self.skipCount += self.avgFrameBetween
        if len(self.stateDelay) == self.historyLength:
            self.statePsnr.pop(0)
            self.stateDelay.pop(0)
            self.stateSkip.pop(0)
        self.statePsnr.append(psnrState)
        self.stateDelay.append(delayState)
        self.stateSkip.append(skipState)
        print("state: ", self.statePsnr, self.stateDelay, self.stateSkip)
        return [psnrState], [delayState], [skipState]


def main():
    stat = [[3, 320], [1, 160], [2, 160]]
    stat2 = [[5, 160], [4, 320], [1, 320], [2, 160]]
    stat2 = [[5, 160], [4, 320], [1, 320], [2, 160]]
    stat2 = [[5, 160], [4, 320], [1, 320], [2, 160]]
    stat2 = [[5, 160], [4, 320], [1, 320], [2, 160]]
    state = ProcessStat()
    state.processPSNR(stat, 0, 1, 4)
    state.processPSNR(stat2, 0, 1,4)
    state.processPSNR(stat2, 0, 1,4)
    state.processPSNR(stat2, 0, 1,4)
    state.processPSNR(stat2, 0, 1,4)


if __name__ == "__main__":
    main()
