import pyautogui
import time
import random
import pyperclip
import os




#sleeps for x       where -1 is 0.01 to 0.1 sec     0 is half a sec or below        2 is 1 sec  3 is 3 sec  5 is 5sec     10 is 10 sec
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

#scrolls with random time delays based on direction, 'U' or 'D' and with x as int for how far.  0- barely moves     1- moves very little        2- normal scroll    3- big scroll like 3 screens        4- top or bottom of page
def rScroll(direction, x):
    time.sleep(2)
    distance = 0
    soFar = 0
    delta = 0

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

    while soFar<distance:
        if random.randint(1,3) == 3:
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
        while soFar+delta > distance:
            delta = delta -1
        soFar = soFar + delta
        if direction == 'U':
            pyautogui.scroll(delta)
        else: pyautogui.scroll(-1*delta)


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

def clearURL():
    moveToUrl()
    sleepTime(-1)
    clickWait(0)
    sleepTime(-1)
    with pyautogui.hold('ctrl'):
        sleepTime(-1)
        pyautogui.press(['a'])
    sleepTime(-1)
    pyautogui.press('backspace')
    sleepTime(-1)

#opens reddit random subreddit, scrolls up then down, then clicks a post and scrolls down slowly to a random point, and repeats with different subs a random number of times less than 3
def redditSurf():
    
    doneNums = []
    xCoord = 0
    yCoord = 0

    for i in range(0, random.randint(1,3)):

        subredditNum = random.randint(1,3)
        while subredditNum in doneNums:
            subredditNum = random.randint(1,3)

        clearURL()
        if subredditNum == 1:
            typeString('reddit.com/r/all')
            xCoord = 898
            yCoord=323
            doneNums.append(1)
        elif subredditNum == 2:
            typeString('reddit.com/r/nba')
            doneNums.append(2)
            xCoord = 944
            yCoord=897
        else:
            typeString('reddit.com/r/manga')
            doneNums.append(3)
            xCoord = 949
            yCoord=769
        pyautogui.press('enter')
        sleepTime(5)
        #scroll down to random point then scrolls to top so we can maybe click post
        rScroll('D', random.randint(1,3))
        sleepTime(1)
        rScroll('D', random.randint(1,3))
        sleepTime(1)
        rScroll('U', 4)
        rMoveTo(xCoord,yCoord)
        clickWait(2)
        #randomly 'look' through comments
        rScroll('D', random.randint(1,3))
        sleepTime(1)
        rScroll('D', random.randint(1,3))
        sleepTime(1)
        rScroll('D', random.randint(1,3))
        sleepTime(1)

    rMoveTo(random.randint(600,700), random.randint(52,55))
    clickWait(-1)

#goes to youtube and hits up to 3 vids from recommended at random. will move mouse to random spot then watch for 5ish sec then cycle
def youtubeSurf():
    clearURL()

    pyautogui.write('y')
    sleepTime(-1)
    pyautogui.press('enter')
    sleepTime(5)
    

    for i in range(1,3):
        vid = random.randint(1,3)

        if vid == 1:
            rMoveTo(random.randint(290,580),random.randint(300,435))
        elif vid == 2:
            rMoveTo(random.randint(1040,1360),random.randint(270,430))
        elif vid == 3:
            rMoveTo(random.randint(1800,2100),random.randint(300,435))    
            
        
        sleepTime(-1)
        clickWait(5)
        rMoveTo(random.randint(100,2300), random.randint(100,1300))
        time.sleep(random.randint(3000,6000)/1000)
        rMoveTo(random.randint(13,30),random.randint(47,62))
        clickWait(5)
    

def copyUrl():
    rMoveTo(random.randint(600,700), random.randint(52,55))
    clickWait(0)
    with pyautogui.hold('ctrl'):
        sleepTime(-1)
        pyautogui.press(['a'])
        sleepTime(-1)
        pyautogui.press(['c'])
    sleepTime(-1)
    return pyperclip.paste()

def forwardButton():
    #hit forward button and wait
            rMoveTo(50+random.randint(-6,6), 53+random.randint(-6,6))
            sleepTime(-1)
            clickWait(5)

def backButton():
    #hit forward button and wait
            rMoveTo(19+random.randint(-6,6), 53+random.randint(-6,6))
            sleepTime(-1)
            clickWait(5)

def newTab():
    rightClickWait(0)
    rMoveTo(xval+35+random.randint(0,10), yval+8+random.randint(0,6))
    sleepTime(-1)
    clickWait(5)

def moveToUrl():
    rMoveTo(random.randint(600,700), random.randint(52,55))

def goToSite(x):
    clearURL()
    typeString(x)
    sleepTime(0)
    pyautogui.press('enter')
    sleepTime(5)

#print(copyUrl())
#youtubeSurf()
#redditSurf()


#LESS GENERIC UTILS FOR READING DESCRIPTION
def tagFormat(input_string):
    # Remove trailing commas and commas at the start
    input_string = input_string.strip(',').lstrip(',')

    # Remove spaces before commas
    while ' ,' in input_string:
        input_string = input_string.replace(' ,', ',')

    # Add a space after each comma
    input_string = input_string.replace(',', ', ')
    
    while ', ' in input_string:
        input_string = input_string.replace(', ', ',')

    input_string = input_string.replace(',', ', ')
    return input_string

def dictionaryMake(firstLine):
    dictionary = {}
    start_index = firstLine.index('[') + 1
    end_index = firstLine.index(']')
    parts = firstLine[start_index:end_index].split('=')

    if parts[4] == 'sticker':
        dictionary['Title'] = parts[0] + ' Sticker'
    else:
        dictionary['Title'] = parts[0]
    dictionary['Desc'] = parts[1].replace('*', '\n')
    dictionary['Tags'] = tagFormat(parts[2])
    dictionary['Colour'] = parts[3]
    dictionary['Product'] = parts[4]

    return dictionary

def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        return len(first_line) == 0

#call this to retrieve the dictionary for data info        
def dataRead():
    empty = is_file_empty('Data.txt')
    if empty:
        return ''
    with open('Data.txt', 'r') as file:
        firstLine = file.readline().strip()
        result = dictionaryMake(firstLine)
        
        return result


def delete_first_line_if_not_empty(file_path):
    if os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            file.writelines(lines[1:])
def delete_lowest_number_file(folder_path):
    file_list = os.listdir(folder_path)
    if file_list:
        lowest_number_file = min(file_list, key=lambda x: int(os.path.splitext(x)[0].split('.')[0]))
        os.remove(os.path.join(folder_path, lowest_number_file))

#USE THIS TO DELETE DATA AFTER POSTING PHOTO ON REDBUBBLE will delete lowest num file in finalPics and the first line in Data.txt
def deleteData():
    data_file_path = "Data.txt"
    delete_first_line_if_not_empty(data_file_path)

    pics_folder_path = "finalPics"
    delete_lowest_number_file(pics_folder_path)

