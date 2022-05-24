import numpy as np


class HandAnalysis:
    def __init__(self, maxnum=5):
        self.maxnum = maxnum
        self.lefthand = []
        self.righthand = []
        self.FingersUpIndex = [4, 8, 12, 16, 20]

    def update(self, hands):
        self.lefthand.append(None)
        self.righthand.append(None)
        for hand in hands:
            p = np.array(hand['lmList'])[self.FingersUpIndex[1:]].mean(axis=0)
            if hand['type'] == 'Right' and self.righthand[-1] is None:
                self.righthand[-1] = p
            if hand['type'] == 'Left' and self.lefthand[-1] is None:
                self.lefthand[-1] = p
        if len(self.lefthand) > self.maxnum:
            self.lefthand = self.lefthand[1:]
        if len(self.righthand) > self.maxnum:
            self.righthand = self.righthand[1:]

    def fingersUp(self, TheHand):
        myHandType = TheHand["type"]
        myLmList = TheHand["lmList"]
        if len(myLmList) > 0:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.FingersUpIndex[0]][0] > myLmList[self.FingersUpIndex[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.FingersUpIndex[0]][0] < myLmList[self.FingersUpIndex[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.FingersUpIndex[id]][1] < myLmList[self.FingersUpIndex[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers
