import imp
import turtle
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(
    mode=False          #maybe try 'true'
    maxHands=1
    detectionCon=0.8
    minTrackCon=0.5
)

while True:
    sucess, img = cap.read()
