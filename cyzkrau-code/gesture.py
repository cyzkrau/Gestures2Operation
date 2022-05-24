import cv2
from HandDetector import HandDetector
import numpy as np
import pyautogui as pg
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
        self.cache = None

    def update_hand(self):
        # judge gestures
        if len(self.hands) == 0:
            return False
        return True

    def update(self):
        sucess, photo = self.cap.read()
        if not sucess:
            print("Error when cap camera")
        photo = cv2.flip(photo, 1)
        self.hands, self.img = self.detector.findHands(photo, flipType=False)
        self.cache = self.detector.cache
        if not self.update_hand():
            self.img = photo
        return False

    def show(self):
        if self.img is not None:
            cv2.imshow('hands', self.img)
            return False
        return True

    def quit(self):
        self.cap.release()


if __name__ == '__main__':
    dect = Gesture_monitor()
    while True:
        order = cv2.waitKey(1)
        x, y = pg.position()
        if dect.update() or dect.show():
            break
        nx, ny, nz = dect.cache
        pg.moveTo(int(x+nx/3), int(y+ny/3))
        if order == 27:
            # press esc to quit
            break
        elif order == ord('c'):
            # press c to capture photo
            cv2.imwrite("imgs/demo" + time.strftime("%m-%d-%H-%M-%S",
                        time.localtime())+".jpg", dect.img)
    dect.quit()
