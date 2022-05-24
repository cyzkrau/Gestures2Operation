# import cv2
# cv2.imshow("win", cv2.imread("../img/example.png"))
# while True:
#     x = cv2.waitKey(1)
#     if x != -1:
#         print(x)
#     if x == ord('x'):
#         break
import numpy as np
SpeedNum = [[1, 2], [3, 4, 5]]
for i in SpeedNum:
    del(i[0])
print(SpeedNum)
