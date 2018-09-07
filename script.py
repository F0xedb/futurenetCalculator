import pyautogui, sys
import time as tm
import math
print('Automating futurenet clicking software v 1.0.0')
print('Press Ctrl-C to quit.')

# timing constants
seconds = 1
minutes= 60 * seconds
hour= 60 * minutes
day= 24* hour

# profile and dashboard coords
dbx=385
dby=106
pfx=473
pfy=106

addx = 570
addy=106

# bookmarklet coords
bm1x=131
bm1y=106
bm2x=270
bm2y=106

# simulates human motion
delay = 0.5

# 30 + loadingdelay
AddDelay = 35 # delay after the add runs
sleep = 4 # howlang you wait between button presses
bisDashboard = True


def center():
    x = 1920/4
    y = 1080/2
    pyautogui.moveTo(x, y, delay)

def bookmarklet1():
    pyautogui.moveTo(bm1x, bm1y, delay)
    pyautogui.click()

def bookmarklet2():
    pyautogui.moveTo(bm2x, bm2y, delay)
    pyautogui.click()

def dashboard():
    pyautogui.moveTo(dbx, dby, delay)
    pyautogui.click()

def profile():
    pyautogui.moveTo(pfx, pfy, delay)
    pyautogui.click()

def watchadd():
    pyautogui.moveTo(addx, addy, delay)
    pyautogui.click()

def toggle():
    global bisDashboard
    if bisDashboard:
        bisDashboard = False
        profile()
    else:
        dashboard()
        bisDashboard = True

def loop():
    print("starting in 5 seconds")
    tm.sleep(5)
    print("starting")
    i = 0
    while i < 11:
        bookmarklet1()
        tm.sleep(sleep)
        center()
        tm.sleep(AddDelay)
        bookmarklet2()
        tm.sleep(sleep)
        i = i + 1


def wait(delay):
    refresh = float(minutes*5)
    i =0
    while i < math.floor(delay/refresh):
        i+=1
        toggle()
        print("toggeling location")
        tm.sleep(refresh)
    toggle()
    tm.sleep((delay%refresh)-5)
    toggle()
    tm.sleep(3)
    dashboard()
    tm.sleep(2)
    watchadd()


def init():
    while True:
        loop()
        delay=float(day + (5*minutes))
        print("delaying for" + str(delay) + " seconds")
        wait(delay)

def positionprint():
    while True:
        print(pyautogui.position())
        tm.sleep(1)
if __name__ == '__main__':
    init()
    #positionprint()

