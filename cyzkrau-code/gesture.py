import cv2
from HandAnalysis import HandAnalysis
import time


if __name__ == '__main__':
    dect = HandAnalysis()
    cap = cv2.VideoCapture(0)
    c = time.time()
    while True:
        sucess, photo = cap.read()
        if not sucess:
            print("Error when cap camera")
            exit(-1)
        photo = cv2.flip(photo, 1)
        image = dect.update(photo)

        cv2.imshow("MOUSE CONTROL", image)
        print(time.time()-c)
        order = cv2.waitKey(1)
        c = time.time()

        # press esc to quit
        if order == 27:
            break

        # x, y = pg.position()
        # nx, ny, nz = dect.point_speed(8, 1)
        # # print(nx, ny, nz)
        # pg.moveTo(int(x+nx), int(y+ny))
    cap.release()
