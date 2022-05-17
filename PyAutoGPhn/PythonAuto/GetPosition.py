import pyautogui as pg
import sys
import time

#设定操作间隔
pg.PAUSE=0.1

print('Press Ctrl-C to Quit.')
try:
    while True:
#   注意位置的传递方法
        x,y = pg.position()
#   注意string的计算
        positionStr = 'X:'+str(x)+',Y:'+str(y)  
        print(positionStr,end='')
#   '\b'应该是backspace
        print('\b'*len(positionStr),end='',flush=True)
        time.sleep(0.1)
except  KeyboardInterrupt:
    print('\n')