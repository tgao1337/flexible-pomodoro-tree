# This is the Flexible Pomodoro Tree official code
 
from threading import Thread, Event, Lock
from pomodoro import *

global mode
global pomoTime
global pomoBreak
global taskNum
global breakBTime
global pressedOnce
global inPomoBreak

global reset
global PlayPauseCheckB
global settingsButton
global settingsSaved
global upButton
global downButton

display = OLED()
display.setup()
display.clear()

dispLock=Lock()

mode = 0  # study mode
pomoTime = 25 * 60  # These are default values
pomoBreak = 5 * 60  # These are default values
inPomoBreak = False
taskNum = 3  # these are default values
currentTask = 1
breakBTime = 60 * 60  # these are default values
pressedOnce = 0 # tracks mode 0 second setting

reset = 0 # 0: Start for the day, 1: End for the day
PlayPauseCheckB = False
settingsButton = False
settingsSaved = False
upButton = False
downButton = False

def checkReset(): # Done for day button
    global reset
    debouncePinB = False
    while True:
        if readButton(pinB):
            if debouncePinB == False:
                debouncePinB = True
                reset = (reset + 1) % 2
                if reset == 0:
                    print("Start for the day")
                else:
                    print("End for the day")
        else:
            debouncePinB = False
    
def checkPlayPauseComplete(): # Play pause check
    global PlayPauseCheckB
    debouncePinA = False
    while True:
        if readButton(pinA):
            if debouncePinA == False:
                debouncePinA = True
                PlayPauseCheckB = not PlayPauseCheckB
                print("Play Pause Complete Button Pressed")
        else:
            debouncePinA = False
    
def checkSettings(): #thread
    global settingsButton
    debouncePinC = False
    while True:
        if readButton(pinC):
            if debouncePinC == False:
                debouncePinC = True
                settingsButton = not settingsButton
                print("Settings Button Pressed")
        else:
            debouncePinC = False
    
def checkUp(): #thread
    global upButton
    debouncePinD = False
    while True:
        if readButton(pinD):
            if debouncePinD == False:
                debouncePinD = True
                upButton = not upButton
                print("Up Button Pressed")
        else:
            debouncePinD = False
    
def checkDown(): #thread
    global downButton
    debouncePinE = False
    while True:
        if readButton(pinE):
            if debouncePinE == False:
                debouncePinE = True
                downButton = not downButton
                print("Down Button Pressed")
        else:
            debouncePinE = False
    
def logic(): #thread
    global reset
    global PlayPauseCheckB
    global settingsButton
    global upButton
    global downButton 
    isSure = False
    
    while True:
        if reset == 1:
            if settingsButton or PlayPauseCheckB: #maybe they can press settings or play button to go into the settings screen?
                settingsButton = False
                PlayPauseCheckB = False
                selection()
                
            
                if settingsButton: #want to update settings more
                    settingsButton = False
                    if mode == 0:
                        pomSett()
                    elif mode == 1:
                        taskSett()
                    elif mode == 2:
                        budgSett()
                    settingsSaved = True
#                     isSure = check()
                        
#                     if isSure:
#                         if mode==0:
#                             goPomo()
#                         if mode==1:
#                             goTask()
#                         if mode==2:
#                             goBudget()
#                     else:
#                         selection()          
            
            else: 
                displayWelcome()  
        else:
            displayWelcome()
            
            
            
def displayWelcome():
    with dispLock:
        print("Welcome! Press Settings to select a mode")
        display.clear()
        # draw tree
        display.draw_line(0, 45, 127 ,45)
        display.text("Welcome", 40, 43, 12)
        display.show()
   
def selection():
    print("In selection menu!")
    global mode
    global upButton
    global downButton
    global settingsButton
    global PlayPauseCheckB
    global settingsSaved
    
    while not settingsButton: #need to press settings or stop start to make a selection
        time.sleep(0.1)
        with dispLock:
            if mode==0:
                display.clear()
                display.text("Select Mode:\n > Pomodoro \n    Task \n    Budget", 20,0,12)
                print("========")
                print("> Pomodoro \n  Task \n  Budget")
                      
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("> Pomodoro", 20,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("Budget", 32,24,14)
                
                
                if downButton:
                    mode = 1
                    downButton = False
                elif upButton:
                    mode = 0
                    upButton = False
                    
            elif mode == 1:
                display.clear()
                display.text("Select Mode:\n    Pomodoro \n > Task \n    Budget", 20,0,12)
                print("========")
                print("  Pomodoro \n> Task \n  Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("> Task", 20,12,14)
#                 display.text("Budget", 32,24,14)
                
                if downButton:
                    mode = 2
                    downButton = False
                elif upButton:
                    mode = 0
                    upButton = False
                    
            elif mode == 2:
                display.clear()
                display.text("Select Mode:\n    Pomodoro \n    Task \n > Budget", 20,0,12)
                print("========")
                print("  Pomodoro \n  Task \n> Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("> Budget", 20,24,14)
                
                if downButton:
                    mode=2
                    downButton = False
                elif upButton:
                    mode = 1
                    upButton = False
                    
            display.show()
    #settingsButton = False

            
def pomSett():
    global upButton
    global downButton
    global settingsButton
    global pomoTime
    global pomoBreak
    
    while not settingsButton:
        with dispLock:
            
            if upButton: 
                upButton = False
                if pomoTime < 7200: #upper limit 2 hours for pomodoro time or shoudl go infintieyl up?
                    pomoTime += 300
            if downButton:
                downButton = False
                if pomoTime >= 600:
                    pomoTime -= 300
                    
            display.clear()
            display.draw_line(0, 45, 127 ,45)
            display.text("P | Settings | 4", 20,45,12)
            
            display.text("Set Work Time:", 25, 0, 12)
            display.text(convertTime(pomoTime), 30, 10, 25)
            display.show()
            
    settingsButton = False
    
    while not settingsButton:
         with dispLock:
            
            if upButton: 
                upButton = False
                if pomoBreak < 3600: #upper limit 1 hours for pomodoro break time ?
                    pomoBreak += 300
            if downButton:
                downButton = False
                if pomoBreak > 300:
                    pomoBreak -= 300
                    
            display.clear()
            display.draw_line(0, 45, 127 ,45)
            display.text("P | Settings | 4", 20,45,12)
            
            display.text("Set Break Time:", 20, 0, 12)
            display.text(convertTime(pomoTime), 30, 10, 25)
            display.show()
            
            
    settingsButton = False
    
def taskSett():
    global upButton
    global downButton
    global settingsButton
    global taskNum
    
    while not settingsButton:
        with dispLock:
             if upButton: 
                  upButton = False
                  if taskNum < 100: #upper limit 100 tasks
                      taskNum += 1
             if downButton:
                  downButton=False
                  if taskNum > 1:
                      taskNum -= 1
             display.clear()
             display.draw_line(0, 45, 127 ,45)
             display.text("T | Settings", 35,45,12)
             display.text("Set Tasks:", 40, 0, 12)
             if taskNum > 9:
                 display.text(str(taskNum), 50, 10, 25)
             else:
                 display.text(str(taskNum), 60, 10, 25)
             display.show()  
             
             
    settingsButton = False
    
def budgSett():
    global upButton
    global downButton
    global settingsButton
    global breakBTime
    
    while not settingsButton:
        with dispLock:
            if upButton: 
                upButton = False
                if breakBTime < 18000: #upper limit 5 hours
                    breakBTime += 600 # maybe more than 10 min increments for this one
            if downButton:
                downButton=False
                if breakBTime > 600:
                    breakBTime -= 600
            display.clear()
            display.draw_line(0, 45, 127 ,45)
            display.text("B | Settings", 35,45,12)
            display.text("Set Break Time:", 20, 0, 12)
            display.text(convertTime(breakBTime), 30, 10,25)
            display.show()     
    settingsButton = False
    
    
def check():
    global mode
    global PlayPauseCheckB
    global settingsButton
    global pomoTime
    global pomoBreak
    global taskNum
    global breakBTime
    
    with dispLock:
        if mode==0:
             display.clear()
             display.text('Flexible Pomodoro Tree', 6, 0)
             display.text('Settings OK ? Press play -->', 12 ,0)
             display.text( 'NO ? press settings', 14, 0)
             display.text('Study' + convertTime(pomoTime), 20, 0)
             display.text('Break' + convertTime(pomoBreak), 24,0)
        if mode ==1:
             display.clear()
             display.text('Flexible Pomodoro Tree', 6, 0)
             display.text('Settings OK ? Press play -->', 12 ,0)
             display.text( 'NO ? press settings', 14, 0)
             display.text('# tasks' + str(taskNum), 20, 0)
        if mode==2:  
             display.clear()
             display.text('Flexible Pomodoro Tree', 6, 0)
             display.text('Settings OK ? Press play -->', 12 ,0)
             display.text( 'NO ? press settings', 14, 0)
             display.text('Total break time' + convertTime(breakBTime), 20, 0)
        display.show()
        
    while True:
        if PlayPauseCheckB:
            PlayPauseCheckB = False
            return True
        if settingsButton:
            settingsButton = False
            return False
                      
def buzzUp():
    playList([(C4, 0.25), (E4, 0.25), (G4, 0.25), (C5, 0.25)])

def buzzDown():
    playList([(C5, 0.25), (G4, 0.25), (E4, 0.25), (C4, 0.25)])
  
  
# ==========================
def Tree():
    global PlayPauseCheckB
    while True:
        if PlayPauseCheckB:
            if mode == 0:
                startPomodoro()
                print("Starting Pomodoro")
            elif mode == 1:
                startTask()
            elif mode == 2:
                startBudget()

def startPomodoro():
    global pomoTime
    global pomoBreak
    global inPomoBreak
    
    if PlayPauseCheckB:
     
        if not inPomoBreak:
            print("Mode: Pomodoro, Work")
            x = pomoTime + 1
            for i in range(x):
                print(convertTime(pomoTime))
                if PlayPauseCheckB == False:
                    break
                pomoTime = pomoTime - 1
                time.sleep(1)
            inPomoBreak = True  # changes to break
            
        if inPomoBreak:
            print("Mode: Pomodoro, Break")
            x = pomoBreak + 1
            for i in range(x):
                print(convertTime(pomoBreak))
                if PlayPauseCheckB == False:
                    break
                pomoBreak = pomoBreak - 1
                time.sleep(1)
            inPomoBreak = False  # changes to work
            


# def resetValues(): # reset the values to default
#     global pomoTime
#     global pomoBreak
#     global taskNum
#     global breakBTime
#     pomoTime = 25*60
#     pomoBreak = 5*60
#     taskNum = 3
#     breakBTime = 5*60

# def checkButtonA():  # changes different modes based on button 3 way toggle
#     global mode
#     risingA = False
#     while True:
#         if readButton(pinA): # 1 button pressed, 0 button not pressed
#             if risingA == False:
#                 risingA = True
#                 mode = (mode + 1) % 4
                
#                 if mode == 0:  # this part needs to rethink. This is to toggle to different modes, not to start the pomodoro or task or budgetBreak. perhaps we have an event so it can run in another thread. I havent fully thought it out but can explain it later.
#                     # i think perhaps this shouldn't be here but in the buttons for startStop. either we have startStop run startPomodoro() or we keep running startPomodoro() and run that in a thread.
#                     # or i think we should have an event as mentioned earlier that puts startPomodoro() in a thread and keeps running it. This way it will keep running in the background even if changed to another mode or setting menu while pomodoro is still going. or we have a lock so they have to finish pomodoro to change setting or go to another mode. that might work better and not be as confusing for the user
#                     startPomodoro()
#                 elif mode == 1:
#                     startTaskMode()
#                 elif mode == 2:
#                     startBBreak()
#         else:
#             risingA = False
            
# def checkButtonR():  # reset button
#     risingR = False
#     while True:
#         if readButton(pinR): # 1 button pressed, 0 button not pressed
#             if risingR == False:
#                 risingR = True
#                 resetValues()
#                 # TODO: stop clock and reset clock
#                 clearAll() # reset LEDs
#         else:
#             risingR = False
            
# def checkButtonE():  # opens settings menu
#     global mode
#     global settingMenu
#     global pressedOnce
#     settingMenu = False
#     risingE = False
#     pressedOnce = 0
    
#     while True:
#         if readButton(pinE): # 1 button pressed, 0 button not pressed
#             if risingE == False:
#                 risingE = True
#                 if mode == 0 and pressedOnce == 1:
#                     pressedOnce = pressedOnce + 1
#                 elif mode == 0:
#                     pressedOnce = pressedOnce + 1
#                     settingMenu = not settingMenu
#                     if pressedOnce > 1:
#                         pressedOnce = 0
#                 else:
#                     settingMenu = not settingMenu
#         else:
#             risingE = False
            
# def countUp():  # count up
#     global mode
#     global settingMenu
#     global pressedOnce
#     global pomoTime
#     global pomoBreak
#     global taskNum
#     global breakBTime
#     risingCntUp = False
    
#     while True:
#         if readButton(pinB): # 1 button pressed, 0 button not pressed
#             if risingCntUp == False and settingMenu:
#                 risingCntUp = True
#                 if mode == 0:
#                     if pressedOnce == 1:
#                         pomoTime+=300 # increment pomo time by 5 min
#                     elif pressedOnce == 2:
#                         pomoBreak+=300 # increment pomo break time by 5 min
#                 elif mode == 1:
#                     taskNum+=1 # increment tasks
#                 else:
#                     breakBTime+=300 # increment break time by 5 min
#         else:
#             risingCntUp = False        
            
# def countDn():  # count down
#     global mode
#     global settingMenu
#     global pressedOnce
#     global pomoTime
#     global pomoBreak
#     global taskNum
#     global breakBTime
#     risingCntDn = False
    
#     while True:
#         if readButton(pinC): # 1 button pressed, 0 button not pressed
#             if risingCntDn == False and settingMenu:
#                 risingCntDn = True
#                 if mode == 0:
#                     if pressedOnce == 1:
#                         pomoTime-=300 # decrement pomo time by 5 min
#                         if pomoTime < 300:
#                             pomoTime = 300
#                     elif pressedOnce == 2:
#                         pomoBreak-=300 # decrement pomo break time by 5 min
#                         if pomoBreak < 300:
#                             pomoBreak = 300
#                 elif mode == 1:
#                     if taskNum > 1:
#                         taskNum-=1 # decrement tasks
#                 else:
#                     breakBTime-=300 # decrement break time by 5 min
#                     if breakBTime < 300:
#                         breakBTime = 300
#         else:
#             risingCntDn = False
            
# def buttonSS():  # button Start Stop
#     global mode
#     global startStop
#     startStop = False
#     risingSS = False
    
#     while True:
#         if readButton(pinSS): # 1 button pressed, 0 button not pressed
#             if risingSS == False:
#                 risingSS = True
#                 startStop = not startStop
#         else:
#             risingSS = False


def convertTime(value):  # given a number of seconds, returns string in HH:MM:SS format
    hours = value // 3600
    minutes = (value % 3600) // 60
    seconds = value % 60
    time = str(hours).ljust(2,'0') + ':' + str(minutes).ljust(2,'0') + ':' + str(seconds).ljust(2,'0')
    return time
            
def updateDisplay():
    global settingsSaved
    while True:
        display.clear()
        if settingsSaved == False:
            if mode == 0:
                display.clear()
                if inPomoBreak:
                    display.text("Break Time:", 25, 0, 12)
                    display.text(convertTime(pomoBreak), 30, 10,25)
                else:
                    display.text("Break Time:", 25, 0, 12)
                    display.text(convertTime(pomoTime), 30, 10,25)
            elif mode == 1:
                    display.text('Tasks:', 30, 0, 12)
                    display.text(str(taskNum), 30, 10, 35) # will need to adjust axes

            elif mode == 2:
                    display.text("Break Time:", 25, 0, 12)
                    display.text(convertTime(breakBTime), 30, 10,25)

            display.show()        
            time.sleep(1)
        
            

t1 = Thread(target=checkReset)
t1.start()

t2 = Thread(target=checkPlayPauseComplete)
t2.start()

t3 = Thread(target=checkSettings)
t3.start()

t4 = Thread(target=checkUp)
t4.start()

t5 = Thread(target=checkDown)
t5.start()

t6 = Thread(target=logic)
t6.start()

t7 = Thread(target=updateDisplay)
t7.start()

t8 = Thread(target=Tree)
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
