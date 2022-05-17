from asyncio.tasks import sleep
from logging import info
import uiautomator2 as ua
import time

#链接小米10s的IP，需要链接在同网络下
#d = ua.connect('10.41.188.211')

d=ua.connect()


def unlock10s():
    d.click(200,1500)
    time.sleep(1)
    d.click(100,1200)
    time.sleep(1)
    d.click(200,1500)
    time.sleep(1)
    d.click(100,1200)
    time.sleep(1)
    d.click(900,1600)
    