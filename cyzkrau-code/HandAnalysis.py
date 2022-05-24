import numpy as np
from HandDetector import HandDetector


class HandAnalysis:
    def __init__(self, SpeedNum=2):
        self.Detector = HandDetector(maxHands=1)
        self.SpeedNum = SpeedNum
        self.CacheHands, self.state = [[], []], ['None', 'None']  # 0 left 1 right
        self.SpeedWeight = np.hstack([-np.ones(int(SpeedNum/2)), np.ones(int(SpeedNum/2))])

    def update(self, image):
        allHands, img = self.Detector.findHands(image, flipType=False)
        for hd in self.CacheHands:
            hd.append(None)
        for hand in allHands:
            p = hand['lmList']
            if hand['type'] == 'Right' and self.CacheHands[1][-1] is None:
                self.CacheHands[1][-1] = p
            if hand['type'] == 'Left' and self.CacheHands[0][-1] is None:
                self.CacheHands[0][-1] = p
        for hd in self.CacheHands:
            if len(hd) > self.SpeedNum:
                del(hd[0])
        return img

    def point_speed(self, point_index, hand_index):
        if None in self.CacheHands[hand_index] or len(self.CacheHands[hand_index]) < self.SpeedNum:
            return [0, 0, 0]
        try:
            p = [hd[point_index] for hd in self.CacheHands[hand_index]]
            return np.dot(self.SpeedWeight, p)/self.SpeedNum
        except:
            print(p)
            print(self.SpeedWeight)
            return [0, 0, 0]


if __name__ == "__main__":
    worker = HandAnalysis()
