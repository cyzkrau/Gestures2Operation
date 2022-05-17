from typing import Text
import pyautogui as pg
import time

#设定操作间隔
pg.PAUSE=0.3

#防故障：pg.FAILSAFE=False
#如果在某个固定位置（最上方）就报错
pg.FAILSAFE=False

#输入选择，最后把选项返回
a=pg.confirm(text='你好吗？',title='问候',buttons=['我很好','我不好','不告诉你'])
print(a)
#同样还有alert,把按钮返回
b=pg.alert(text='tql!',title='系统提示',button='tql!')
print(b)

c=pg.prompt(text = '现在怎么样:',title='密码输入',default='')
print(c)

d=pg.password(text='请输入密码',title='密码',default='',mask='$')
print(d)

#都是以用户点击的作为返回值