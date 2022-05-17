from asyncio.tasks import sleep
from logging import info
import uiautomator2 as ua
import time

#链接小米10s的IP，需要链接在同网络下
d = ua.connect('192.168.43.40')

#d=ua.connect()
d(resourceId="com.miui.home:id/icon_icon", description="微信").click()

time.sleep(3)

d(resourceId="com.tencent.mm:id/dub", text="发现").click()

time.sleep(3)

d(resourceId="com.tencent.mm:id/h6o").click()

time.sleep(3)

d.xpath('//*[@resource-id="com.tencent.mm:id/hzr"]/android.widget.RelativeLayout[5]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click_exists()

time.sleep(3)

d(resourceId="com.tencent.mm:id/ka").click_exists()


#d.xpath('//*[@resource-id="com.tencent.mm:id/hzr"]/android.widget.RelativeLayout[！i！]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click_exists()一般格式
