#!/usr/bin/python3
import cv2
from cvzone.HandTrackingModule import HandDetector
import time


class GestureMonitor:

    def __init__(self, width=1280, height=720):
        self.cap = cv2.VideoCapture(0)
        self.width = width
        self.height = height
        self.cap.set(3, width)
        self.cap.set(4, height)

        self.detector = HandDetector()
        self.img = None
        self.hands = None

        self.physical_condition = {
            'IsLeft': False,
            'IsRight': False,
            'IsUp': False,
            'IsDown': False,
            'Is1&2': False
        }

    def update(self):
        sucess, self.img = self.cap.read()
        if sucess != True:
            print("Error when cap camera")
        self.img = cv2.flip(self.img, 1)
        self.hands, self.img = self.detector.findHands(self.img,
                                                       flipType=False)
        hand = self.hands[0]['lmList']
        if hand[0][0] > hand[12][0]:
            self.physical_condition['IsLeft'] = True
            self.physical_condition['IsRight'] = False
        elif hand[0][0] < hand[12][0]:
            self.physical_condition['IsLeft'] = False
            self.physical_condition['IsRight'] = True

        if hand[9][1] < hand[12][1]:
            self.physical_condition['IsDown'] = True
            self.physical_condition['IsUp'] = False
        elif hand[9][1] > hand[12][1]:
            self.physical_condition['IsDown'] = False
            self.physical_condition['IsUp'] = True
        if abs(hand[8][0] - hand[12][0]) + abs(hand[8][1] - hand[12][1]):
            self.physical_condition['Is1&2'] = True
        else:
            self.physical_condition['Is1&2'] = False

    def show(self):
        cv2.imshow('hands', self.img)

    def is_left(self):
        return self.physical_condition['IsLeft']

    def is_right(self):
        return self.physical_condition['IsRight']

    def is_up(self):
        return self.physical_condition['IsUp']

    def is_down(self):
        return self.physical_condition['IsDown']

    def is_push(self):
        return self.physical_condition['Is1a2']

    def quit(self):
        self.cap.release()


'''
def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = HandDetector()
    i = 0
    while True:
        sucess, img = cap.read()
        if sucess != True:
            print("Error when cap camera")
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        i = i + 1
        if i % 100 == 0:
            print(hands)
            print(type(hands))
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
'''
'''
dect = gesture_monitor()
while True:
    dect.update()
    dect.show()
    print("Is left? {}".format(dect.is_left()))
    print("Is right? {}".format(dect.is_right()))
    print("Is up?{}".format(dect.is_up()))
    print("is down?{}".format(dect.is_down()))
    if cv2.waitKey(1) & 0xFF == 27:
        break
dect.quit()
'''