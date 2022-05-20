import pyautogui as pg
import time

'''
#获取屏幕像素
print(pg.size())
width,height = pg.size()
print(width,height)
'''
#将im获取为当前屏幕
im=pg.screenshot()
#im.getpixel((500,500))是位置上的RGB值
#print(im.getpixel((500,500)))

#保存截图
#im.save('屏幕截图.png')

#对比颜色 指定位置与指定颜色的
#print(pg.pixelMatchesColor(500,500,(12,120,240)))

#搜索位置,一个的情况 返回(left= ,top= ,width= ,height= ), pg.center可以直接返回目标的中心
btm=pg.locateOnScreen('Zan.png')
pg.dragTo(pg.center(btm),duration=0.5)
pg.click(button='left')
'''
#还不太懂列表的数据类型
atm=pg.locateAllOnScreen('S.png')
print(atm)
'''