import pyautogui as pg
import time


#设定操作间隔
pg.PAUSE=0.1


# 定位到Windows的位置
pg.dragTo(100,1060,0.2)
pg.click()



'''
#敲击键盘
pg.press('k') # 敲击一个键
pg.hotkey('ctrl','v') #热键（快捷方式输入）
pg.hotkey('ctrl','a')  #热键（快捷方式输入）
pg.press('backspace') #删除
'''

'''
pg.keyDown() #按住不放
pg.keyUp() #将键盘松下
pg.keyDown('alt')
pg.press('tab',interval=0.1)
pg.keyUp('alt')
'''
'''
#写字
pg.write('hello world!',interval=0.1)
'''
pg.hotkey('shift')
pg.write('nihaoa',interval=0.1)
pg.dragTo(100,1020,0.2)
pg.click(button='left')
pg.press('enter')