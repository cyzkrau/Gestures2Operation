# import cv2
# cv2.imshow("win", cv2.imread("../img/example.png"))
# while True:
#     x = cv2.waitKey(1)
#     if x != -1:
#         print(x)
#     if x == ord('x'):
#         break
import time
import pyautogui as pg
import cv2
pg.PAUSE = 0.005


def main():
    a = time.time()
    # pg.moveRel(-200, -200)
    # pg.click()
    cv2.waitKey(1)
    print(time.time()-a)


main()
main()
main()
