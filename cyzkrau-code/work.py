# import cv2
# cv2.imshow("win", cv2.imread("../img/example.png"))
# while True:
#     x = cv2.waitKey(1)
#     if x != -1:
#         print(x)
#     if x == ord('x'):
#         break
import pyautogui as pg
while True:
    print(pg.position())
