import pyautogui as pg
import time

pg.click(100,1060,interval=0.3)#打开Windows全局搜索
pg.write('https://weixine.ustc.edu.cn/2020/login#\n',interval=0.1)#在全局搜索中输入网址
time.sleep(3)#等待浏览器响应
pg.moveTo(777,931)#到可以点上报的位置
pg.scroll(-1000)#向下翻
time.sleep(1)#等浏览器响应
pg.click(777,931)#点击
time.sleep(2)#暂停稍许
pg.click(1900,15)#关闭浏览器