import pyautogui
import time
import random
import pyperclip
import os




#sleeps for x       where -1 is 0.01 to 0.1 sec     0 is half a sec or below    1 is for 1 sec    3 is 3 sec  5 is 5sec     10 is 10 sec
def sleepTime(x):
    if x == -1:
        ret = float(random.randint(10,100))
        time.sleep(ret/1000)
    if x == 0:
        ret = float(random.randint(100,500))
        time.sleep(ret/1000)
        return
    elif x == 1:
        ret = float(random.randint(100,1000))
        time.sleep(ret/1000)
        return
    elif x == 3:
        ret = float(random.randint(2500,3500))
        time.sleep(ret/1000)
        return
    elif x == 5:
        ret = float(random.randint(4500,5500))
        time.sleep(ret/1000)
        return
    elif x == 10:
        ret = float(random.randint(5000,10000))
        time.sleep(ret/1000)
        return

#clicks and waits for time depending on x       where -1 is 0.01 to 0.1 sec     0 is half a sec or below        2 is 1 sec  3 is 3 sec      10 is 10 sec
def clickWait(x):
    pyautogui.click()
    sleepTime(x)
    return

#above but right
def rightClickWait(x):
    pyautogui.rightClick()
    sleepTime(x)
    return

#moves to location x y with a bunch of somewhat randomized small movements and random very tiny waits
def rMoveTo(x,y):
    x,y = unpercent(x,y)
    cx, cy = pyautogui.position()

    #set vars to see if we are starting below or above the target
    xHigh = False
    yHigh = False
    if cx >= x: 
        xHigh = True
    if cy >= y:
        yHigh = True

    #set movement speed based on distance
    maxX = 30
    minX = 8
    maxY = 30
    minY = 8

    if abs(cx-x) > 500:
        maxX = maxX*2
        minX = minX*2
        if abs(cx-x) > 1000:
            maxX = maxX*2
            minX = minX*2
            if abs(cx-x) > 1700:
                maxX = maxX*2
                minX = minX*2
    
    if abs(cy-y) > 500:
        maxY = maxY*2
        minY = minY*2
        if abs(cy-y) > 1000:
            maxY = maxY*2
            minY = minY*2

    while cx != x or cy != y:
        deltaX = 0
        deltaY = 0
        #print('cx is ', cx, 'cy is ', cy, 'and goal x and y are ', x , y)

        
        #small movement
        #check if we need to move x at all, if so by rand int to 5 and if we overshoot then reverse
        if cx != x:
            if xHigh:   #we're too high, subtract
                deltaX = random.randint(-1*maxX,-1*minX)
                while cx+deltaX-x < 0:  #overshot condition
                    deltaX = deltaX +1
            else:   #too low, increase
                deltaX = random.randint(minX,maxX)
                while cx+deltaX-x > 0:  #overshot condition
                    deltaX = deltaX -1
        
        #check if we need to move y at all, if so by rand int to 5 and if we overshoot then reverse
        if cy != y:
            if yHigh:   #we're too high, subtract
                deltaY = random.randint(-1*maxY,-1*minY)
                while cy+deltaY-y < 0:  #overshot condition
                    deltaY = deltaY +1
            else:   #too low, increase
                deltaY = random.randint(minY,maxY)
                while cy+deltaY-y > 0:  #overshot condition
                    deltaY = deltaY -1

        #do movement
        pyautogui.move(deltaX, deltaY)
        if random.randint(1,3) == 2:
            sleepTime(-1)

        cx, cy = pyautogui.position()


#types out word with -1 sleeptime in between chars
def typeString(word):
    for i in word:
        pyautogui.write(i)
        sleepTime(-1)
    sleepTime(1)



def rScrollReturn(direction, x):
    time.sleep(2)
    distance = 0
    soFar = 0
    delta = 0
    ret = 0
    if x == 0:
        distance = random.randint(80,120)
    elif x == 1:
        distance = random.randint(700,800)
    elif x == 2:
        distance = random.randint(1500, 8000)
    elif x == 3:
        distance = random.randint(10000, 30000)
    elif x == 4:
        distance = random.randint(200000, 300000)
    elif x == 10:
        distance = random.randint(1495, 1500)
    elif x == 11:
        distance = random.randint(100, 108)

    while soFar<distance:        
        sleepTime(-1)
        if x == 0:
            delta = random.randint(10,30)
        elif x == 1:
            delta = random.randint(50,300)
        elif x == 2:
            delta = random.randint(300,1000)
        elif x == 3:
            delta = random.randint(1000,8000)    
        elif x == 4:
            delta = random.randint(10000,80000)    
        elif x == 10:
            delta = random.randint(50,100)
        elif x == 11:
            delta = random.randint(10,20)
        while soFar+delta > distance:
            delta = delta -1
        soFar = soFar + delta
        if direction == 'U':
            pyautogui.scroll(delta)
        else:
            pyautogui.scroll(-1*delta)
        ret+= delta
            
    return ret

#clears text 
def clearText():
    sleepTime(-1)
    clickWait(0)
    sleepTime(-1)
    with pyautogui.hold('ctrl'):
        sleepTime(-1)
        pyautogui.press(['a'])
    sleepTime(-1)
    pyautogui.press('backspace')
    sleepTime(-1)

def perctenter(pos):
    x = pos[0]/pyautogui.size()[0]*100
    y = pos[1]/pyautogui.size()[1]*100
    return (round(x, 2), round(y, 2))
    
def unpercent(x,y):
    maxx = pyautogui.size()[0]
    maxy = pyautogui.size()[1]
    x = round(x*maxx/100)
    y = round(y*maxy/100)
    return (x,y)


def f():
    time.sleep(1)
    print(perctenter(pyautogui.position()))


f()