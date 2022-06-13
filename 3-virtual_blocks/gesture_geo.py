import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

cx, cy, w, h = 200, 200, 200, 200
color = (150, 0, 150)


def distant(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


class Obstacle():

    def __init__(self,
                 posCenter,
                 size=[200, 200],
                 type="rectangle",
                 color=(100, 0, 100)):
        self.posCenter = posCenter
        self.size = size
        self.type = type
        self.color = color

    def update(self, img, cursor1, cursor2, cursor3):
        color = self.color
        if self.posCenter[0] - self.size[0] // 2 < cursor1[
                0] < self.posCenter[0] + self.size[0] // 2 and self.posCenter[
                    1] - self.size[1] // 2 < cursor1[
                        1] << self.posCenter[1] + self.size[1] // 2:
            color = (100, 0, 0)
            if distant(cursor_1, cursor_2) < 90:
                color = (0, 255, 0)
                self.posCenter = ((cursor1[0] + cursor2[0]) // 2,
                                  (cursor1[1] + cursor2[1]) // 2)
        cv2.rectangle(img, (self.posCenter[0] - self.size[0] // 2,
                            self.posCenter[1] - self.size[1] // 2),
                      (self.posCenter[0] + self.size[0] // 2,
                       self.posCenter[1] + self.size[1] // 2), color,
                      cv2.FILLED)
        return img

    def draw(self, img):
        cv2.rectangle(img, (self.posCenter[0] - self.size[0] // 2,
                            self.posCenter[1] - self.size[1] // 2),
                      (self.posCenter[0] + self.size[0] // 2,
                       self.posCenter[1] + self.size[1] // 2), self.color,
                      cv2.FILLED)
        return img


rectList = []
for i in range(3):
    rectList.append(Obstacle((i * 250 + 150, 250)))

while True:
    sucess, img = cap.read()
    img = cv2.flip(img, 1)
    hand, img = detector.findHands(img)
    if hand:
        lmList = hand[0]['lmList']
        cursor_1 = lmList[8]
        cursor_2 = lmList[12]
        cursor_3 = lmList[4]
        for rect in rectList:
            img = rect.update(img, cursor_1, cursor_2, cursor_3)
    else:
        for rect in rectList:
            img = rect.draw(img)

    cv2.imshow("image", img)
    cv2.waitKey(1)
