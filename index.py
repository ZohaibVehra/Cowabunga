from Utils import *
import time
import math


spotifyPin = (25.59, 98.47)
start_time = None

def start_tracking_time():
    global start_time
    start_time = time.time()

def stop_tracking_time():
    global start_time 
    if start_time is None:
        print("Error: Call start_tracking_time() first.")
        return

    elapsed_time = time.time() - start_time
    start_time = None  # Reset start_time for future calls
    return elapsed_time

def startSpotify():
    rMoveTo(spotifyPin[0],spotifyPin[1])
    clickWait(3)
    

def startList():
    rMoveTo(7.58, 28.61)
    time.sleep(1)
    clickWait(1)
    time.sleep(1)
    rMoveTo(18.95, 43.26)
    sleepTime(1)
    clickWait(-1)
    start_tracking_time()
    
def mininize():
    rMoveTo(spotifyPin[0],spotifyPin[1])
    clickWait(2)


def stopListening():
    rMoveTo(19.06, 34.24)
    time.sleep(1)
    clickWait(-1)
    ret = stop_tracking_time()
    rMoveTo(99.14, 1.46)
    time.sleep(1)
    clickWait(1)
    return ret

    


start_time = None

listens = 0

for i in range(7): 

    startSpotify()
    startList()
    mininize()
    random_minutes = random.uniform(0, 1)
    random_seconds = random.randint(0, 20)
    total_seconds = random_minutes * 60 + random_seconds   
    time.sleep(random_seconds)
    startSpotify()
    sec = stopListening()
    listens = listens + math.floor(sec/402)
    print(listens)
    random_minutes = random.uniform(0, 2)
    random_seconds = random.randint(0, 30)
    total_seconds = random_minutes * 60 + random_seconds 
    time.sleep(total_seconds)

print("final = "+listens)