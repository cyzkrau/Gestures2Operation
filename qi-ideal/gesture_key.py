import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller


class Button():

    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size


def draw(img, button, color=(255, 0)):
    x, y = button.pos
    w, h = button.size
    cv2.rectangle(img, (x, y), (x + w, y + h), color, cv2.FILLED)
    cvzone.cornerRect(
        img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
        20,
        rt=0,
        colorC=(100, 0, 0))
    cv2.putText(img, button.text, (x + 25, y + 60), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 255, 255), 3)
    return img


def drawkeys(img, buttonLists):
    for button in buttonLists:
        draw(img, button)
    return img


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "!"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", " ", ",", ".", "^"]]

buttonList = []

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

key_string = ""
key_last = ""
moved = False
shifted = 1

keyboard = Controller()

while True:
    sucess, img = cap.read()
    img = cv2.flip(img, 1)

    hand, img = detector.findHands(img)
    drawkeys(img, buttonList)
    if hand:
        lmList = hand[0]['lmList']
        bboxInfo = hand[0]['bbox']
        if lmList:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    # to make double input possible
                    if button.text != key_last:
                        moved = True
                    img = draw(img, button, color=(128, 0, 0))
                    if x < lmList[12][0] < x + w and y < lmList[12][1] < y + h:
                        img = draw(img, button, color=(0, 255, 0))
                        if moved or key_last != button.text:
                            if button.text == "<":
                                key_string = key_string[0:-1]
                                keyboard.press(Key.backspace)
                            elif button.text == "^":
                                shifted = (shifted + 1) % 2
                            else:
                                if button.text.isalpha() and shifted:
                                    key_string += button.text.lower()
                                    keyboard.press(button.text.lower())
                                else:
                                    key_string += button.text
                                    keyboard.press(button.text)
                            moved = False
                        key_last = button.text

    cv2.rectangle(img, (50, 450), (1135, 550), (175, 0, 0), cv2.FILLED)
    cv2.putText(img, key_string + "|", (60, 525), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 255, 255), 5)
    cv2.imshow("image", img)
    cv2.waitKey(1)