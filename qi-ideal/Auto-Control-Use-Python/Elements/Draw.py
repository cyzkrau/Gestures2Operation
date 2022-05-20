import pyautogui as pg
import time

pg.click(10,1060,interval=0.2)
pg.write('huatu\n',interval=0.1)
time.sleep(1)
pg.moveTo(250,250)
LengthY=520
LengthX=520
Delta=10
n=int((LengthX/Delta)/2)
for i in range(n):
    pg.dragRel(0,LengthY)
    LengthY=LengthY-Delta
    pg.dragRel(LengthX,0)
    LengthX=LengthX-Delta
    pg.dragRel(0,-LengthY)
    LengthY=LengthY-Delta
    pg.dragRel(-LengthX,0)
    LengthX=LengthX-Delta