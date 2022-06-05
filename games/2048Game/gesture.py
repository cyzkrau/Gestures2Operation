#!/usr/bin/python3
from shutil import move
import cv2
from cv2 import selectROI
from cv2 import sepFilter2D
from cvzone.HandTrackingModule import HandDetector
import time

from pymacaroons import MACAROON_V1
from sympy import elliptic_f, re


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

        self.v_last_condi = None
        self.v_this_condi = None
        self.h_last_condi = None
        self.h_this_condi = None

    def update(self):
        sucess, self.img = self.cap.read()
        if sucess != True:
            print("Error when cap camera")
        self.img = cv2.flip(self.img, 1)
        self.hands, self.img = self.detector.findHands(self.img,
                                                       flipType=False)
        try:
            hand = self.hands[0]['lmList']
            # The 2-4 hand is hand[12][0]
            self.v_last_condi = self.v_this_condi
            self.h_last_condi = self.h_this_condi

            if hand[0][0] > hand[12][0]:
                self.physical_condition['IsLeft'] = True
                self.physical_condition['IsRight'] = False
                self.h_this_condi = "a"
            elif hand[0][0] < hand[12][0]:
                self.physical_condition['IsLeft'] = False
                self.physical_condition['IsRight'] = True
                self.h_this_condi = "d"

            if hand[9][1] < hand[12][1]:
                self.physical_condition['IsDown'] = True
                self.physical_condition['IsUp'] = False
                self.h_this_condi = "s"
            elif hand[9][1] > hand[12][1]:
                self.physical_condition['IsDown'] = False
                self.physical_condition['IsUp'] = True
                self.h_this_condi = "w"
        except:
            print("No Hand Dectable.")

    def show(self):
        cv2.imshow('hands', self.img)
        cv2.waitKey(1)

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

    def move_v(self):
        if self.v_last_condi != self.v_this_condi:
            return self.v_this_condi
        else:
            return None

    def move_h(self):
        if self.h_last_condi != self.h_this_condi:
            return self.h_this_condi
        else:
            return None

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