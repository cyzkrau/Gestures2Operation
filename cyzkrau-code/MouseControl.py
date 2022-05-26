import cv2
from HandAnalysis import HandAnalysis
import pyautogui as pg
import time


if __name__ == '__main__':
    pg.PAUSE = 0.005
    dect = HandAnalysis(4)
    cap = cv2.VideoCapture(0)
    c = time.time()
    drag = False
    while True:
        sucess, photo = cap.read()
        if not sucess:
            print("Error when cap camera")
            exit(-1)
        photo = cv2.flip(photo, 1)
        image = dect.update(photo)

        cv2.imshow("MOUSE CONTROL", image)
        # print(time.time()-c)
        order = cv2.waitKey(1)
        # c = time.time()

        # press esc to quit
        if order == 27:
            break
        # print(dect.UpOrDown)
        drag = (dect.UpOrDown[0][0] == 1)

        nx, ny, nz = dect.point_speed(8, 1)
        # print(nz)
        # print(nx, ny, nz)
        if drag:
            pg.dragRel(2*int(nx), 2*int(ny), button='left')
        else:
            pg.moveRel(2*int(nx), 2*int(ny))
    cap.release()
