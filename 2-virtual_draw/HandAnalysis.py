import numpy as np
from HandDetector import HandDetector


class HandAnalysis:
    def __init__(self, SpeedNum=10):
        self.Detector = HandDetector(maxHands=2)
        self.SpeedNum = SpeedNum
        self.CacheHands, self.state = [[], []], ['None', 'None']  # 0 left 1 right
        self.NormalState = {}
        self.SpeedWeight = np.hstack([-np.ones(int(SpeedNum/2)), np.ones(int(SpeedNum/2))])
        self.UpOrDown = [[0]*5, [0]*5]

    def update(self, image):
        allHands, img = self.Detector.findHands(image, flipType=False)
        for hd in self.CacheHands:
            hd.append(None)
        for hand in allHands:
            p = hand['lmList']
            if hand['type'] == 'Right' and self.CacheHands[1][-1] is None:
                self.CacheHands[1][-1] = p
                self.UpOrDown[1] = self.Detector.fingersUp(hand)
            if hand['type'] == 'Left' and self.CacheHands[0][-1] is None:
                self.CacheHands[0][-1] = p
                self.UpOrDown[0] = self.Detector.fingersUp(hand)
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

    def hand_direction(self, hand_index, check=False):
        # where
        if None in self.CacheHands[hand_index] or len(self.CacheHands[hand_index]) < self.SpeedNum:
            return 0
        hands = np.array(self.CacheHands[hand_index][-1])
        diff = (hands[8]-hands[5])[:-1]
        speed = self.point_speed(8, hand_index)[:-1]
        if check:
            self.NormalState[str(hand_index)] = diff
            return 0
        else:
            if np.linalg.norm(speed) < 10:
                return 0
            diff = diff - self.NormalState[str(hand_index)]
            if np.linalg.norm(diff) < 100:
                return 0
            ind_speed = 0 if abs(speed[0]) > abs(speed[1]) else 1
            ind_state = 0 if abs(diff[0]) > abs(diff[1]) else 1
            if ind_speed != ind_state or speed[ind_speed]*diff[ind_state] < 0:
                return 0
            return 2+np.sign(speed[ind_speed])+ind_speed


if __name__ == "__main__":
    worker = HandAnalysis()
