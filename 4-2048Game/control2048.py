import cv2
from HandAnalysis import HandAnalysis
import pyautogui as pg
import time


if __name__ == '__main__':
    pg.PAUSE = 0.005
    dect = HandAnalysis(6)
    cap = cv2.VideoCapture(0)
    c = time.time()
    drag = True
    pasm = 0
    ans = ['left', 'up', 'right', 'down']
    while True:
        sucess, photo = cap.read()
        if not sucess:
            print("Error when cap camera")
            exit(-1)
        photo = cv2.flip(photo, 1)
        image = dect.update(photo)

        cv2.imshow("KEYBOARD CONTROL", image)
        # print(time.time()-c)
        order = cv2.waitKey(1)
        # c = time.time()

        # press esc to quit and c to end change mode
        if order == 27:
            break
        if order == ord("c"):
            drag = not drag

        newm = dect.hand_direction(1, drag)
        if newm == 0 or pasm != 0:
            pasm = newm
            continue
        pasm = newm
        pg.press(ans[int(pasm)-1])
        # print(ans[int(pasm)-1])
    cap.release()
