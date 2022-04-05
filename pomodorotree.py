# This is the Flexible Pomodoro Tree official code

from threading import Thread, Event, Lock
from pomodoro import *

global mode
global buttonA
global pomoTime
global pomoBreak
global taskNum
global breakBTime
global pressedOnce
mode = 0
buttonA = 0
pomoTime = 25 * 60  # these are default values
pomoBreak = 5 * 60  # these are default values
taskNum = 3  # these are default values
breakBTime = 60 * 60  # these are default values
pressedOnce = 0 # tracks mode 0 second setting

def buzzUp():
    playList([(C4, 0.25), (E4, 0.25), (G4, 0.25), (C5, 0.25)])

def buzzDown():
    playList([(C5, 0.25), (G4, 0.25), (E4, 0.25), (C4, 0.25)])

def setup_display():
    pass

def startPomodoro():
    print("pomodoro!")
    
def startBBreak():
    print("budget break")

def startTaskMode():
    print("task mode")
    
def pomodoroBreak():
    pass

def checkButtonA():  # changes different modes based on button 3 way toggle
    global mode
    risingA = False
    
    while True:
        if readButton(pinA): # 1 button pressed, 0 button not pressed
            if risingA == False:
                risingA = True
                mode = (mode + 1) % 3:
        else:
            risingA = False
            
def checkButtonE():  # opens settings menu
    global mode
    global settingMenu
    global pressedOnce
    settingMenu = False
    risingE = False
    pressedOnce = 0
    
    while True:
        if readButton(pinE): # 1 button pressed, 0 button not pressed
            if risingE == False:
                risingE = True
                if mode == 0 and pressedOnce == 1:
                    pressedOnce = pressedOnce + 1
                elif mode == 0:
                    pressedOnce = pressedOnce + 1
                    settingMenu = not settingMenu
                    if pressedOnce > 1:
                        pressedOnce = 0
                else:
                    settingMenu = not settingMenu
        else:
            risingE = False
            
def countUp():  # count up
    global mode
    global settingMenu
    global pressedOnce
    global pomoTime
    global pomoBreak
    global taskNum
    global breakBTime
    risingCntUp = False
    
    while True:
        if readButton(pinB): # 1 button pressed, 0 button not pressed
            if risingCntUp == False and settingMenu:
                risingCntUp = True
                if mode == 0:
                    if pressedOnce == 1:
                        pomoTime+=300 # increment pomo time by 5 min
                    elif pressedOnce == 2:
                        pomoBreak+=300 # increment pomo break time by 5 min
                elif mode == 1:
                    taskNum+=1 # increment tasks
                else:
                    breakBTime+=300 # increment break time by 5 min
        else:
            risingCntUp = False        
            
def countDn():  # count down
    global mode
    global settingMenu
    global pressedOnce
    global pomoTime
    global pomoBreak
    global taskNum
    global breakBTime
    risingCntDn = False
    
    while True:
        if readButton(pinC): # 1 button pressed, 0 button not pressed
            if risingCntDn == False and settingMenu:
                risingCntDn = True
                if mode == 0:
                    if pressedOnce == 1:
                        pomoTime-=300 # decrement pomo time by 5 min
                        if pomoTime < 300:
                            pomoTime = 300
                    elif pressedOnce == 2:
                        pomoBreak-=300 # decrement pomo break time by 5 min
                        if pomoBreak < 300:
                            pomoBreak = 300
                elif mode == 1:
                    if taskNum > 1:
                        taskNum-=1 # decrement tasks
                else:
                    breakBTime-=300 # decrement break time by 5 min
                    if breakBTime < 300:
                        breakBTime = 300
        else:
            risingCntDn = False
            
def buttonSS():  # button Start Stop
    global mode
    global startStop
    startStop = False
    risingSS = False
    
    while True:
        if readButton(pinSS): # 1 button pressed, 0 button not pressed
            if risingSS == False:
                risingSS = True
                startStop = not startStop
        else:
            risingSS = False

t1 = Thread(target=checkButtonA)
t1.start()
t2 = Thread(target=checkButtonE)
t2.start()
t3 = Thread(target=countUp)
t3.start()
t4 = Thread(target=countDn)
t4.start()
t5 = Thread(target=buttonSS)
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
