# refer to https://github.com/cvzone
import cv2
import mediapipe as mp
import numpy as np
import math


class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """

    def __init__(self, mode=False, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon
        self.MaxHandNum = 6

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=2,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.CacheHands, self.state = [[], []], ['None', 'None']  # 0 left 1 right
        self.fingers = []
        self.tipIds = [4, 8, 12, 16, 20]
        # self.SpeedWeight = np.array([-1, -1, -1, 1, 1, 1])
        self.SpeedWeight = np.array([0, 0, 0, 0, -1, 1])
        self.cache = None

    def findHands(self, img, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}
                # lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])
                    xList.append(px)
                    yList.append(py)

                # bbox
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                    bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] = (cx, cy)

                if flipType:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

        # cache
        self.CacheHands[0].append(None)
        self.CacheHands[1].append(None)
        for hand in allHands:
            p = hand['lmList']
            if hand['type'] == 'Right' and self.CacheHands[1][-1] is None:
                self.CacheHands[1][-1] = p
            if hand['type'] == 'Left' and self.CacheHands[0][-1] is None:
                self.CacheHands[0][-1] = p
        for i in range(2):
            if len(self.CacheHands[i]) > self.MaxHandNum:
                self.CacheHands[i] = self.CacheHands[i][1:]
        self.update_state()
        if draw:
            for hand in allHands:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                bbox = hand['bbox']
                state = self.state[0] if hand['type'] == 'Left' else self.state[1]
                cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20), (bbox[0] +
                              bbox[2] + 20, bbox[1] + bbox[3] + 20), (255, 0, 255), 2)
                cv2.putText(img, state, (bbox[0] - 30, bbox[1] - 30),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            return allHands, img
        return allHands

    def update_state(self, mode='Pointing'):
        if mode == "Moving":
            for i in range(2):
                if (len(self.CacheHands[i]) < self.MaxHandNum) or (None in self.CacheHands[i]):
                    self.state[i] = 'None'
                else:
                    hands = np.array(self.CacheHands[i])
                    speed = np.dot(self.SpeedWeight, hands)[:-1]
                    if np.linalg.norm(speed) > 200:
                        # print(speed)
                        ind = ['Left', 'Right', 'Up', 'Down']
                        w = np.argmax(np.abs(speed))
                        self.state[i] = ind[int(2*w+(speed[w] > 0))]
                    else:
                        self.state[i] = 'None'
        elif mode == 'Pointing':
            if (len(self.CacheHands[1]) == self.MaxHandNum) and (None not in self.CacheHands[1]):
                point = [k[8] for k in self.CacheHands[1]]
                self.cache = np.dot(self.SpeedWeight, point)
            else:
                self.cache = [0, 0, 0]

    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers


def main():
    ori_img = cv2.imread("imgs/demo.jpg")
    detector = HandDetector(detectionCon=0.8)

    hands, img = detector.findHands(ori_img, flipType=False)

    hand1 = hands[0]
    lmList1 = hand1["lmList"]  # List of 21 Landmark points
    bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
    centerPoint1 = hand1['center']  # center of the hand cx,cy
    handType1 = hand1["type"]  # Handtype Left or Right

    fingers1 = detector.fingersUp(hand1)
    import numpy as np
    print(np.array(lmList1)[[8, 12, 16, 20]].mean(axis=0))
    # print(np.dot(np.ones(4)/4, lmList1[[8, 12, 16, 20]]))

    # cv2.imshow("Image", img)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
