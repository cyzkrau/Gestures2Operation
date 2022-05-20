import imp
import pyautogui as pg
import time
import tkinter
import gesture
import cv2

screen = tkinter.Tk()

screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

monitor = gesture.Gesture_monitor(width=screen_width, height=screen_height)

while True:
    monitor.update()
    monitor.show()
    x, y = monitor.get_pos_l24()
    if x != -1:
        pg.moveTo(x * screen_width, y * screen_height)
        if monitor.is_push():
            print("push!")
            pg.click(x * screen_width, y * screen_height)
    if cv2.waitKey(1) & 0xFF == 27:
        break
'''
pg.click(10, 1060, interval=0.2)
pg.write('huatu\n', interval=0.1)
time.sleep(1)
pg.moveTo(250, 250)
LengthY = 520
LengthX = 520
Delta = 10
n = int((LengthX / Delta) / 2)
for i in range(n):
    pg.dragRel(0, LengthY)
    LengthY = LengthY - Delta
    pg.dragRel(LengthX, 0)
    LengthX = LengthX - Delta
    pg.dragRel(0, -LengthY)
    LengthY = LengthY - Delta
    pg.dragRel(-LengthX, 0)
    LengthX = LengthX - Delta
'''