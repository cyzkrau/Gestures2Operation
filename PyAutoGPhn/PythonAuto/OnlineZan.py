import pyautogui as pg
import time

#设定操作间隔
pg.PAUSE=0.3

#防故障：pg.FAILSAFE=False
#如果在某个固定位置（最上方）就报错
pg.FAILSAFE=False

while True:
    time.sleep(1)
    zan=pg.locateOnScreen('Zan.png')
    if zan != None:
        pg.click(pg.center(zan))
        print('Done one')
    pg.scroll(-400)