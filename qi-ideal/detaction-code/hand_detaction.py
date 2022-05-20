#!/usr/bin/python3
import cv2
from cvzone.HandTrackingModule import HandDetector  # 手部检测方法
import time

#（1）导数视频数据
cap = cv2.VideoCapture(0)  # 0代表自己电脑的摄像头
cap.set(3, 280)  # 设置显示框的宽度1280
cap.set(4, 20)  # 设置显示框的高度720

pTime = 0  # 设置第一帧开始处理的起始时间

#（2）接收手部检测方法
detector = HandDetector(
    mode=False,  # 视频流图像 
    maxHands=2,  # 最多检测一只手
    detectionCon=0.8,  # 最小检测置信度 
    minTrackCon=0.5)  # 最小跟踪置信度

cv2.startWindowThread()

#（3）处理每一帧图像
#i = 0
while True:

    # 图片是否成功接收、img帧图像
    success, img = cap.read()
    if success != True:
        print("ERROR DETECTION!")
    # 翻转图像，使自身和摄像头中的自己呈镜像关系
    img = cv2.flip(img, flipCode=2)  # 1代表水平翻转，0代表竖直翻转

    #（4）手部检测方法
    # 传入每帧图像, 返回手部关键点的坐标信息(字典构成的列表hands)，绘制关键点后的图像img
    hands, img = detector.findHands(img, flipType=False)  # 上面反转过了，这里就不用再翻转了

    #print("the {} th".format(i), hands)
    #i = i + 1

    #（5）显示图像
    # 查看FPS
    #cTime = time.time()  #处理完一帧图像的时间
    #fps = 1 / (cTime - pTime)
    #pTime = cTime  #重置起始时间

    # 在视频上显示fps信息，先转换成整数再变成字符串形式，文本显示坐标，文本字体，文本大小
    #cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    #            (255, 0, 0), 3)

    # 显示图像，输入窗口名及图像数据
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:  #每帧滞留20毫秒后消失，ESC键退出
        break

# 释放视频资源
cap.release()
cv2.destroyAllWindows()