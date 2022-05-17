from asyncio.tasks import sleep
from logging import info
from types import prepare_class
from typing import Text
import uiautomator2 as ua
import time

#链接小米10s的IP，需要链接在同网络下
#d = ua.connect('10.41.188.211')

#USB直接链接，需要之由一个选项，并且手机打开开发者选项-->USB调试
d=ua.connect()

'''
d.debug = True      #打开调试开关
d.info
'''

'''#和APP操作有关
#引号为包名称,获取方法：长按APP，信息，信息(i)（应用详情）
#打开应用-->等5秒-->关闭应用
d.app_start('com.tencent.mm') 
time.sleep(5)
d.app_stop('com.tencent.mm')
'''


'''#和应用相关
print('窗口大小：',d.window_size())
#显示设备窗口分辨率,和设备垂直与水平有关

print('当前APP:',d.app_current())

print('序列号：',d.serial)
#输出序列号

print('Wifi IP:',d.wlan_ip)
#获取链接的WIFI的IP

print('设备信息：',d.device_info)
#获取设备的信息
'''

'''
#有关APP信息
print('APP信息：',d.app_info('com.tencent.mm'))
'''

#和屏幕操作有关！！！
#d.screen_on()           #打开屏幕
#d.unlock()          #解锁，必须是要在手机息屏下用，不稳定
#d.click(600,1000)       #点击像素坐标  d.click(x,y)
#d.double_click(900,1600,0.1)
#d.screen_off()
#d.swipe(200,1000,400,1000,duration=0.05)    #滑动   d.swipe(start_x, start_y, end_x, end_y,duration)
#d.drag(100,1000,900,1000,duration=2)        #和上面那个一样
#d.long_click(0.5,0.5,duration=2)   #长按，使用百分比
#d.long_click(500,1000,duration=2)    #长按，使用屏幕坐标

#d.press("home") # 点击home键
#d.press("back") # 点击back键

#d.press("menu") # 点击menu按键,任务管理
#d.press("recent") # 点击近期活动按键


#d.press("search") # 点击搜索按键,手机全局搜索
#d.press("enter") # 点击enter键
#d.press("delete") # 点击删除按键


#d.press("volume_up") # 音量+
#d.press("volume_down") # 音量-
#d.press("volume_mute") # 静音
#d.press("power") #电源键


'''
#(q1,q2)=(100,1200),(z1,z2)=(200,1500),(e1,e2)=(900,1600)
#d.screen_on()
#time.sleep(1)
#d.swipe(500,100,100,100)
d.unlock()
time.sleep(1)
d.click(200,1500)
time.sleep(1)
d.click(100,1200)
time.sleep(1)
d.click(200,1500)
time.sleep(1)
d.click(100,1200)
time.sleep(1)
d.click(900,1600)
#q=(100,1200),z=(200,1500),enter=(900,1600)
'''

d(description='微信').click()
d(className='android.widget.ImageView').click()