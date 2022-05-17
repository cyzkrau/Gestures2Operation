#!/usr/bin/python3
from ctypes.wintypes import HENHMETAFILE
from lib2to3.pytree import type_repr
from opcode import hasname
from turtle import update
import cv2
from cv2 import exp
from cvzone.HandTrackingModule import HandDetector
import time


class Gesture_monitor:

    def __init__(self, width=1280, height=720):
        self.cap = cv2.VideoCapture(0)
        self.size = {'width': width, 'height': height}
        self.cap.set(3, width)
        self.cap.set(4, height)

        self.detector = HandDetector()
        self.img = None
        self.hands = None

        self.phy_cond = {
            'IsLeft': False,
            'IsRight': False,
            'IsUp': False,
            'IsDown': False,
            'Is1a2': False
        }

    def update_hand(self, hand):
        if hand[0][0] > hand[12][0]:
            self.phy_cond['IsLeft'] = True
            self.phy_cond['IsRight'] = False
        elif hand[0][0] < hand[12][0]:
            self.phy_cond['IsLeft'] = False
            self.phy_cond['IsRight'] = True

        if hand[9][1] < hand[12][1]:
            self.phy_cond['IsDown'] = True
            self.phy_cond['IsUp'] = False
        elif hand[9][1] > hand[12][1]:
            self.phy_cond['IsDown'] = False
            self.phy_cond['IsUp'] = True
        print(hand[8], hand[12])
        #print(
        #    abs(hand[8][0] - hand[12][0]) < 30,
        #    abs(hand[8][1] - hand[12][1]) < 30)
        is1a2 = abs(hand[8][0] - hand[12][0]) < 50 & abs(
            hand[8][1] - hand[12][1]) < 50 & abs(hand[8][2] - hand[12][2]) < 50
        print(is1a2)
        if abs(hand[8][0] -
               hand[12][0]) < 40 & abs(hand[8][1] - hand[12][1]) < 40 & abs(
                   hand[8][2] - hand[12][2]) < 40:
            self.phy_cond['Is1a2'] = True
        else:
            self.phy_cond['Is1a2'] = False

    def update(self):
        sucess, photo = self.cap.read()
        if sucess != True:
            print("Error when cap camera")
        #print("ok before flip")
        photo = cv2.flip(photo, 1)
        #print("ok before hand dect")
        self.hands, self.img = self.detector.findHands(photo, flipType=False)
        try:
            hand = self.hands[0]['lmList']
            self.update_hand(hand)
        except:
            self.img = photo
        # print(self.hands)
        '''                                               
        hand = self.hands[0]['lmList']  #need 'try catch' here
        if hand[0][0] > hand[12][0]:
            self.phy_cond['IsLeft'] = True
            self.phy_cond['IsRight'] = False
        elif hand[0][0] < hand[12][0]:
            self.phy_cond['IsLeft'] = False
            self.phy_cond['IsRight'] = True

        if hand[9][1] < hand[12][1]:
            self.phy_cond['IsDown'] = True
            self.phy_cond['IsUp'] = False
        elif hand[9][1] > hand[12][1]:
            self.phy_cond['IsDown'] = False
            self.phy_cond['IsUp'] = True
        '''

    def is_left(self):
        return self.phy_cond['IsLeft']

    def is_right(self):
        return self.phy_cond['IsRight']

    def is_up(self):
        return self.phy_cond['IsUp']

    def is_down(self):
        return self.phy_cond['IsDown']

    def is_push(self):
        return self.phy_cond['Is1a2']

    def get_pos_l24(self):
        ret = [0, 0]
        try:
            ret[0] = self.hands[0]['lmList'][8][0] / self.size['width']
            ret[1] = self.hands[0]['lmList'][8][1] / self.size['height']
        except:
            ret[0] = -1
            ret[1] = -1
        return ret

    def show(self):
        # print(self.hands)
        cv2.imshow('hands', self.img)

    def quit(self):
        self.cap.release()


if __name__ == '__main__':
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

    #'''
    dect = Gesture_monitor()
    i = 0
    while True:
        dect.update()
        dect.show()
        i = i + 1
        print(dect.is_push())
        if i % 50 == 0:
            print(dect.get_pos_l24())
        if cv2.waitKey(1) & 0xFF == 27:
            break
    dect.quit()
#'''