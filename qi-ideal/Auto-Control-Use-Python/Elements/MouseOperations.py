import pyautogui as pg
import sys
import time

#设定操作间隔
pg.PAUSE=0.1

'''
#可以左(left),右(right),中间(middle)
pg.click(button='right')

#移动到，不拖拽 pg.moveTo(x,y,time)
pg.moveTo(238,124)

#移动到，需要拖拽(会默认左键) pg.dragTo(x,y,time,buttom='left/right'{同时是否左，右托鼠标})
pg.dragTo(238,124,0.5)
'''
'''
#鼠标向量加，(x,y) x轴向右，y轴向下，duration是持续时长
pg.moveRel(500,100,duration=1)
pg.dragRel(100,500,duration=1)
'''
'''
#鼠标滚动 pg.scroll(数字) 以像素为单位，+上，-下
pg.scroll(-300)
'''