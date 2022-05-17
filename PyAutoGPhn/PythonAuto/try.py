import pyautogui as pg

RY1=(0,-415)
RY2=(0,-345)
RY3=(0,-295)
RY=[RY1,RY2,RY3]
RQZone=(214,-467)

Duration = 0.2
n=5000

def OpenThreeZones(Posit):
    for R in RY:
        pg.click(Posit)
        pg.moveRel(R,duration=Duration)
        pg.click()
        pg.moveTo(Posit)
        pg.moveRel(RQZone,duration=Duration)
        pg.click()
    return 1

def CloseEdge():
    for i in range(10):
        pg.click(1687,24,interval=Duration/2,duration=Duration)
    for i in range(2):
        pg.click(1236,24,interval=Duration/2,duration=Duration)
    

Q1=(414+2,600+2)
Q2=(352+2,562+2)
Q3=(292+2,521+2)
Q4=(232+2,485+2)
QS=[Q1,Q2,Q3,Q4]

for i in range(n):
    for Q in QS:
        OpenThreeZones(Q)
    pg.sleep(5)
    CloseEdge()