# This is the Flexible Pomodoro Tree official code
 
from threading import Thread, Event, Lock
from pomodoro import *

global mode
global pomoTime
global pomoBreak
global taskNum
global breakBTime
global pressedOnce
global inBreak

global offB
global startStopB
global settB
global upB
global downB

dispLock=Lock()

mode = 0  # study mode
pomoTime = 25 * 60  # these are default values
pomoBreak = 5 * 60  # these are default values
inBreak = 0
taskNum = 3  # these are default values
currentTask = 1
breakBTime = 60 * 60  # these are default values
pressedOnce = 0 # tracks mode 0 second setting

offB=False
startStopB = False
settB= False
upB=False
downB=False

def checkOFF(): #thread
    global offB
    
    while True:
        if readpin(offPin):
            offB=True
    time.sleep(1)
    
def checkStrt(): #thread
    global startStopB
    
    while True:
        if readpin(startPin):
           startStopB=True
    time.sleep(1)
    
def checkSett(): #thread
    global settB
    
    while True:
        if readpin(settPin):
            settB=True
    time.sleep(1)
    
def checkUp(): #thread
    global upB
    
    while True:
        if readpin(upPin):
            upB=True
    time.sleep(1)
    
def checkDown(): #thread
    global downB
    
    while True:
        if readpin(downPin):
            downB=True
    time.sleep(1)
    
def logic(): #thread
    global offB
    global startStopB
    global settB
    global upB
    global downB 
    isSure=False
    
    while True:
        if not offB:
            if settB or startStopB: #maybe they can press settings or play button to go into the settings screen?
                settB=False
                startStopB=False
                selection()
                
                if startStopB: #pressed play button from sttings selection, want to use preset values
                    startStopB= False
                    isSure= check()
                    
                    if isSure:
                        if mode==0:
                            goPomo()
                        if mode==1:
                            goTask()
                        if mode==2:
                            goBudget()
                    else:
                        selection()
            
                else if settB: #want to update settings more
                    settB=False
                    if mode==0:
                        pomSett()
                    else if mode==1:
                        taskSett()
                    else:
                        budgSett()
                    
                    isSure=check()
                        
                    if isSure:
                        if mode==0:
                            goPomo()
                        if mode==1:
                            goTask()
                        if mode==2:
                            goBudget()
                    else:
                        selection()          
            
            else: 
                welcome()  
        else:
            welcome()
            
            
            
def welcome():
    with dispLock:
        display.clear()
        display.write('Flexible Pomodoro Tree', 6, 0)
        display.write("Welcome", 15,0)
        display.show()

def selection():
    global mode
    global upB
    global downB
    global settB
    global startStopB
    
    while not settB and not startStopB: #need to press settings or stop start to make a selection
        with dispLock:
            if mode==0:
                display.clear()
                display.write('Flexible Pomodoro Tree', 6, 0)
                display.write(' > Pomodoro Mode', 12,0)
                display.write(' Task Mode', 14,0)
                display.write(' Budget Mode', 16,0)
                
                if upB:
                    mode=1
                    upB=False
                else if downB():
                    mode=0
                    downB=False
            else if mode==1:
                display.clear()
                display.write('Flexible Pomodoro Tree', 6, 0)
                display.write(' Pomodoro Mode', 12,0)
                display.write(' > Task Mode', 14,0)
                display.write(' Budget Mode', 16,0)
                
                if upB:
                    mode=2
                    upB=False
                else if downB():
                    mode=0
                    downB=False
            else if mode ==2:
              display.clear()
                display.write('Flexible Pomodoro Tree', 6, 0)
                display.write(' Pomodoro Mode', 12,0)
                display.write(' Task Mode', 14,0)
                display.write(' > Budget Mode', 16,0)
                
                if upB:
                    mode=2
                    upB=False
                else if downB():
                    mode=1
                    DownB=False
                    
            display.show()
            
def pomSett():
    global upB
    global downB
    global settB
    global pomoTime
    global pomoBreak
    
    while not settB:
        with dispLock:
            
            if upB: 
                upB=False
                if pomoTime< 7200: #upper limit 2 hours for pomodoro time or shoudl go infintieyl up?
                    pomoTime +=300
            if downB:
                downB=False
                if pomoTime>=600:
                    pomoTime-=300
                    
            display.clear()
            display.write('Flexible Pomodoro Tree', 6, 0)
            display.write('Set Work Time', 10, 0)
            display.write(convert(pomoTime), 25, 0)
            display.show()
            
    settB=False
    while not settB:
         with dispLock:
            
            if upB: 
                upB=False
                if pomoBreak < 3600: #upper limit 1 hours for pomodoro break time ?
                    pomoBreak +=300
            if downB:
                downB=False
                if pomoBreak >300:
                    pomoBreak-=300
                    
            display.clear()
            display.write('Flexible Pomodoro Tree', 6, 0)
            display.write('Set Break Time', 10, 0)
            display.write(convert(pomoBreak), 25, 0)
            display.show()
    settB=False
    
def taskSett():
    global upB
    global downB
    global settB
    global taskNum
    
    while not settB:
        with dispLock:
             if upB: 
                  upB=False
                  if taskNum < 100: #upper limit 100 tasks
                      taskNum +=1
             if downB:
                  downB=False
                  if taskNum >1:
                      taskNum-=1
             display.clear()
             display.write('Flexible Pomodoro Tree', 6, 0)
             display.write('Set Num Tasks', 10, 0)
             display.write(str(taskNum), 25, 0)
             display.show()     
    settB=False
    
def budgSett():
    global upB
    global downB
    global settB
    global breakBTime
    
    while not settB:
        with dispLock:
            if upB: 
                  upB=False
                  if breakBTime < 18000: #upper limit 5 hours
                      breakBTime +=300 #maybe more tan 5 min increments for this one? 
             if downB:
                  downB=False
                  if breakBTime >300:
                      breakBTime-=300
             display.clear()
             display.write('Flexible Pomodoro Tree', 6, 0)
             display.write('Set Total Break Time', 10, 0)
             display.write(convert(breakBTime), 25, 0)
             display.show()     
    settB=False
    
    
def check():
    global mode
    global startstopB
    global settB
    global pomoTime
    global pomoBreak
    global taskNum
    global breakBTime
    
    with dispLock:
        if mode==0:
             display.clear()
             display.write('Flexible Pomodoro Tree', 6, 0)
             display.write('Settings OK ? Press play -->', 12 ,0)
             display.write( 'NO ? press settings, 14, 0)
             display.write('Study' + convert(pomoTime), 20, 0)
             display.write('Break' + convert(pomoBreak), 24,0)
        if mode ==1:
             display.clear()
             display.write('Flexible Pomodoro Tree', 6, 0)
             display.write('Settings OK ? Press play -->', 12 ,0)
             display.write( 'NO ? press settings, 14, 0)
             display.write('# tasks' + str(taskNum), 20, 0)
        if mode==2:  
             display.clear()
             display.write('Flexible Pomodoro Tree', 6, 0)
             display.write('Settings OK ? Press play -->', 12 ,0)
             display.write( 'NO ? press settings, 14, 0)
             display.write('Total break time' + convert(breakBTime), 20, 0)
        while not startStopB and not settB:
            display.show()
            if startStopB:
               startStopB=False
               return True
            if settB:
               settB=False
               return False
                       #smthn is weird below here whenever U try to make a function here it doesnt like it i cant find space issue
 ########################################################################################################                         
                           
def buzzUp():
    playList([(C4, 0.25), (E4, 0.25), (G4, 0.25), (C5, 0.25)])

def buzzDown():
    playList([(C5, 0.25), (G4, 0.25), (E4, 0.25), (C4, 0.25)])

def setup_display():
    display = OLED()
    display.setup()
    display.clear()
    # Drawing a border
    display.draw_line(0, 0, 127 ,0)
    display.draw_line(0, 0, 0 ,63)
    display.draw_line(0, 63, 127 ,63)
    display.draw_line(127, 0, 127 ,63)
    # Making a line
    display.draw_line(0, 12, 127 ,12)
    
    # Pomodoro text
    display.write('Flexible Pomodoro Tree', 6, 0):
    display.show()

def startPomodoro():
    global pomoTime
    global pomoBreak
    
    if mode == 0 and startStop: # this needs to check if the pomo session is actually started. review code
        print("pomodoro!")
        if inBreak:
            x = pomoBreak + 1
            for i in range(x):
                if startStop == False:
                    break
                pomoBreak = pomoBreak - 1
                time.sleep(1)
            inBreak = 0  # changes to pomo
            
        else:  # do we need an else? or can we do "elif not inBreak and mode == 0 and startStop"?
            x = pomoTime + 1
            for i in range(x):
                if startStop == False:
                    break
                pomoTime = pomoTime - 1
                time.sleep(1)
            inBreak = 1  # changes to break
            startPomodoro()
    
def startTaskMode():
    if mode == 1:
        print("task mode")

def startBBreak():
    if mode == 2:
        print("budget break")
    
def pomodoroBreak():
    pass

def resetValues(): # reset the values to default
    global pomoTime
    global pomoBreak
    global taskNum
    global breakBTime
    pomoTime = 25*60
    pomoBreak = 5*60
    taskNum = 3
    breakBTime = 5*60

def checkButtonA():  # changes different modes based on button 3 way toggle
    global mode
    risingA = False
    while True:
        if readButton(pinA): # 1 button pressed, 0 button not pressed
            if risingA == False:
                risingA = True
                mode = (mode + 1) % 4:
                
                ```if mode == 0:  # this part needs to rethink. This is to toggle to different modes, not to start the pomodoro or task or budgetBreak. perhaps we have an event so it can run in another thread. I havent fully thought it out but can explain it later.
                    # i think perhaps this shouldn't be here but in the buttons for startStop. either we have startStop run startPomodoro() or we keep running startPomodoro() and run that in a thread.
                    # or i think we should have an event as mentioned earlier that puts startPomodoro() in a thread and keeps running it. This way it will keep running in the background even if changed to another mode or setting menu while pomodoro is still going. or we have a lock so they have to finish pomodoro to change setting or go to another mode. that might work better and not be as confusing for the user
                    startPomodoro()
                elif mode == 1:
                    startTaskMode()
                elif mode == 2:
                    startBBreak()```
        else:
            risingA = False
            
def checkButtonR():  # reset button
    risingR = False
    while True:
        if readButton(pinR): # 1 button pressed, 0 button not pressed
            if risingR == False:
                risingR = True
                resetValues()
                # TODO: stop clock and reset clock
                clearAll() # reset LEDs
        else:
            risingR = False
            
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


def convertTime(value):  # given a number of seconds, returns string in HH:MM:SS format
    hours = value // 3600
    minutes = (value % 3600) // 60
    seconds = value % 60
    time = str(hours) + ':' + str(minutes) + ':' + str(seconds)
    return time
            
def updateDisplay():
    while True:
        setup_display()
        if mode == 0:
            display.clear()
            if inBreak:
                display.write('Remaining break time:', 20, 0)
                display.write(convertTime(pomoBreak), 30, 0) # will need to adjust axes
            else:
                display.write('Remaining work time:', 20, 0)
                display.write(convertTime(pomoTime), 30, 0) # will need to adjust axes
        elif mode == 1:
                display.write('Remaining tasks:', 20, 0):
                display.write(taskNum, 30, 0) # will need to adjust axes
                display.write('Working on task:', 40, 0):
                display.write(currentTask, 50, 0) # will need to adjust axes
        elif mode == 2:
                display.write('Remaining break time:', 20, 0):
                display.write(convertTime(breakBTime), 30, 0) # will need to adjust axes

        display.show()        
        time.sleep(1)
        
            

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
t6 = Thread(target=updateDisplay)
t6.start()

# TODO: Threads to add later:
#    display check if settingMenu or display mode
#    reset button

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
