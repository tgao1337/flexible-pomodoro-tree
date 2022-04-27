# This is the Flexible Pomodoro Tree official code
 
from threading import Thread, Event, Lock
from pomodoro import *

global mode
global pomoWorkTime
global pomoBreakTime
global taskNum
global budgetTime
global pressedOnce
global inPomoBreak
global resetRequired
global playPauseCheckB
global settingsButton
global settingsSaved
global upButton
global downButton
# user set times
global uPomoWTime
global uPomoBTime
global uTaskNum
global uBudgetTime

# display = OLED()
# display.setup()
# display.clear()

dispLock=Lock()
eventSettings = Event()

mode = 0  # study mode
pomoWorkTime = 25 * 60  # These are default values
pomoBreakTime = 5 * 60  # These are default values
taskNum = 4  # these are default values
budgetTime = 60 * 60  # these are default values
# changed when user modifies the following, also used to reset values to these
uPomoWTime = 25 * 60
uPomoBTime = 5 * 60
uTaskNum = 4
uBudgetTime = 60 * 60

inPomoBreak = False
currentTask = 1
pressedOnce = 0 # tracks mode 0 second setting

resetRequired = False # True: Start for the day, False: End for the day
playPauseCheckB = False
settingsButton = False
settingsSaved = False
upButton = False
downButton = False

def checkReset(): # Done for day button
    global resetRequired
    debouncePinB = False
    while True:
        if readButton(pinB):
            if debouncePinB == False:
                debouncePinB = True
                resetRequired = not resetRequired
                if resetRequired:
                    print("Start for the day")
                else:
                    print("End for the day")
        else:
            debouncePinB = False
    
def checkPlayPauseComplete(): # Play pause check
    global playPauseCheckB
    debouncePinA = False
    while True:
        if readButton(pinA):
            if debouncePinA == False:
                debouncePinA = True
                playPauseCheckB = not playPauseCheckB
                print("Play Pause Complete Button Pressed")
        else:
            debouncePinA = False
    
def checkSettings():
    global settingsButton
    global settingsSaved 
    global resetRequired
    debouncePinC = False
    while True:
        if readButton(pinC):
            if debouncePinC == False:
                debouncePinC = True
                settingsSaved = False # Whenever Settings button is pressed change settingsSaved to False
                print("resetRequired:", resetRequired)
                if resetRequired:
                    print("settingButtons set to True")
                    settingsButton = True
#                     eventSettings.set()
                else: 
                    print("settingButtons set to False")
                    settingsButton = False
                print("Settings Button Pressed: " , settingsButton)
                
             
        else:
            debouncePinC = False
    
def checkUp(): #thread
    global upButton
    debouncePinD = False
    while True:
        if readButton(pinD):
            if debouncePinD == False:
                debouncePinD = True
                upButton = True
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
                downButton = True
                print("Down Button Pressed")
        else:
            debouncePinE = False
    
def logic(): #thread
    print("Thread running: logic")
    global reset
    global playPauseCheckB
    global settingsButton
    global upButton
    global downButton 
    isSure = False
    
    while True:
        if settingsButton:
            settingsButton = False
            result = selection()
            if result == 0:
                pomSett()
            elif result == 1:
                taskSett()
            elif result == 2:
                budgSett()
              
        if playPauseCheckB and settingsSaved: # If the playPauseCheckB has been pressed and settingsSaved start Tree
            if mode == 0:
                startPomodoro()
                print("Starting Pomodoro now!")
            elif mode == 1:
                startTask()
            elif mode == 2:
                startBudget()
        
#         if reset: # Start for the day, begin with selecting mode but wait for settings button being pressed
#             event.wait()
#             if settingsButton: # if settings button pressed go into selection
#                 settingsButton = False
#                 result = selection()
#                 if result == 0:
#                     pomSett()
#                 elif result == 1:
#                     taskSett()
#                 elif result == 2:
#                     budgSett()

#                 if settingsButton: #want to update settings more
#                     settingsButton = False
#                 if mode == 0:
#                     pomSett()
#                 elif mode == 1:
#                     taskSett()
#                 elif mode == 2:
#                     budgSett()

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
            
#             else: 
#                 displayWelcome()  
#         else:
#             displayWelcome()
           
            
def displayWelcome():
    with dispLock:
        print("Welcome! Press Start and Settings to select a mode")
#         display.clear()
# #         draw tree
#         display.draw_line(0, 45, 127 ,45)
#         display.text("Welcome", 40, 43, 12)
#         display.show()
   
def selection():
    print("Please select a mode from the following:")
    global mode
    global upButton
    global downButton
    global settingsButton
    global playPauseCheckB
    global settingsSaved
    
    print("> Pomodoro \n  Task \n  Budget")
    modeChangeDetected = False
    while True:
        with dispLock:
            if mode == 0:
                #display.clear()
                #display.text("Select Mode:\n > Pomodoro \n    Task \n    Budget", 20,0,12)
                #display.show()
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("> Pomodoro \n  Task \n  Budget")
                      
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("> Pomodoro", 20,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("Budget", 32,24,14)
                
                if downButton:
                    mode = 1
                    downButton = False
                    modeChangeDetected = True
                elif upButton:
                    mode = 0
                    upButton = False
                    modeChangeDetected = True
                if settingsButton:
                    settingsButton = False
                    print("POMODORO MODE SELECTED")
                    return 0

                
            elif mode == 1:
                #display.clear()
                #display.text("Select Mode:\n    Pomodoro \n > Task \n    Budget", 20,0,12)
                #display.show()
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("  Pomodoro \n> Task \n  Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("> Task", 20,12,14)
#                 display.text("Budget", 32,24,14)
                
                if downButton:
                    mode = 2
                    downButton = False
                    modeChangeDetected = True
                elif upButton:
                    mode = 0
                    upButton = False
                    modeChangeDetected = True
                if settingsButton:
                    settingsButton = False
                    print("TASK MODE SELECTED")
                    return 1
              
                
            elif mode == 2:
                #display.clear()
                #display.text("Select Mode:\n    Pomodoro \n    Task \n > Budget", 20,0,12)
                #display.show()
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")            
                    print("  Pomodoro \n  Task \n> Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("> Budget", 20,24,14)
                
                if downButton:
                    mode=2
                    downButton = False
                    modeChangeDetected = True
                elif upButton:
                    mode = 1
                    upButton = False
                    modeChangeDetected = True
                if settingsButton:
                    settingsButton = False
                    print("BUDGET MODE SELECTED")
                    return 2

def pomSett():
    print("In Pomodoro Settings")
    global upButton
    global downButton
    global settingsButton
    global settingsSaved
    global pomoWorkTime
    global pomoBreakTime
    global uPomoWTime
    global uPomoBTime
    
    print("Please set the work time. Current work time:", pomoWorkTime)
    while not settingsButton: # If settingsButton is not pressed keep changing pomoWorkTime
        with dispLock:
            
            if upButton: 
                upButton = False
                if pomoWorkTime < 7200: #upper limit 2 hours for pomodoro time or shoudl go infintieyl up?
                    pomoWorkTime += 300
                    print("New work time:", pomoWorkTime)
            if downButton:
                downButton = False
                if pomoWorkTime >= 600:
                    pomoWorkTime -= 300
                    print("New work time:", pomoWorkTime)

            #display.clear()
            #display.draw_line(0, 45, 127 ,45)
            #display.text("P | Settings | 4", 20,45,12)
            
            #display.text("Set Work Time:", 25, 0, 12)
            #display.text(convertTime(pomoWorkTime), 30, 10, 25)
            #display.show()
            
    settingsButton = False
    print("WORK TIME SET TO:", pomoWorkTime)

    print("Please set the break time. Current break time:", pomoBreakTime)
    while not settingsButton:
         with dispLock:
            
            if upButton: 
                upButton = False
                if pomoBreakTime < 3600: #upper limit 1 hours for pomodoro break time ?
                    pomoBreakTime += 300
                    print("New break time:", pomoBreakTime)
            if downButton:
                downButton = False
                if pomoBreakTime > 300:
                    pomoBreakTime -= 300
                    print("New break time:", pomoBreakTime)
                    
#             display.clear()
#             display.draw_line(0, 45, 127 ,45)
#             display.text("P | Settings | 4", 20,45,12)
            
#             display.text("Set Break Time:", 20, 0, 12)
#             display.text(convertTime(pomoWorkTime), 30, 10, 25)
#             display.show()
   
    settingsButton = False
    print("BREAK TIME SET TO:", pomoBreakTime)
    uPomoWTime = pomoWorkTime
    uPomoBTime = pomoBreakTime
    settingsSaved = True
    print("Settings have been saved", settingsSaved)

def taskSett():
    global upButton
    global downButton
    global settingsButton
    global taskNum
    global settingsSaved
    global uTaskNum
    
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
    uTaskNum = taskNum
    settingsSaved = True
       
def budgSett():
    global upButton
    global downButton
    global settingsButton
    global budgetTime
    global settingsSaved
    global uBudgetTime
    
    while not settingsButton:
        with dispLock:
            if upButton: 
                upButton = False
                if budgetTime < 18000: #upper limit 5 hours
                    budgetTime += 600 # maybe more than 10 min increments for this one
            if downButton:
                downButton=False
                if budgetTime > 600:
                    budgetTime -= 600
            display.clear()
            display.draw_line(0, 45, 127 ,45)
            display.text("B | Settings", 35,45,12)
            display.text("Set Break Time:", 20, 0, 12)
            display.text(convertTime(budgetTime), 30, 10,25)
            display.show()     
    settingsButton = False
    uBudgetTime = budgetTime
    settingsSaved = True

'''
# ignore
def check():
    global mode
    global playPauseCheckB
    global settingsButton
    global pomoWorkTime
    global pomoBreakTime
    global taskNum
    global budgetTime
    
    with dispLock:
        if mode==0:
             display.clear()
             display.text('Flexible Pomodoro Tree', 6, 0)
             display.text('Settings OK ? Press play -->', 12 ,0)
             display.text( 'NO ? press settings', 14, 0)
             display.text('Study' + convertTime(pomoWorkTime), 20, 0)
             display.text('Break' + convertTime(pomoBreakTime), 24,0)
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
             display.text('Total break time' + convertTime(budgetTime), 20, 0)
        display.show()
        
    while True:
        if playPauseCheckB:
            playPauseCheckB = False
            return True
        if settingsButton:
            settingsButton = False
            return False
'''
def buzzUp():
    playList([(C4, 0.25), (E4, 0.25), (G4, 0.25), (C5, 0.25)])

def buzzDown():
    playList([(C5, 0.25), (G4, 0.25), (E4, 0.25), (C4, 0.25)])
  
  
# ==========================
# def Tree():
#     global playPauseCheckB
#     global settingsSaved
#     while True:
#         if playPauseCheckB and settingsSaved:
#             if mode == 0:
#                 startPomodoro()
#                 print("Starting Pomodoro")
#             elif mode == 1:
#                 startTask()
#             elif mode == 2:
#                 startBudget()

def startPomodoro():
    global pomoWorkTime
    global pomoBreakTime
    global inPomoBreak
    
    if playPauseCheckB:
        if not inPomoBreak:
            print("Mode: Pomodoro, Work")
            x = pomoWorkTime + 1
            
            for i in range(x):
                print(convertTime(pomoWorkTime))
                if playPauseCheckB == False:
                    return
                pomoWorkTime = pomoWorkTime - 1
                time.sleep(1)
            inPomoBreak = True  # changes to break
            
        if inPomoBreak:
            print("Mode: Pomodoro, Break")
            x = pomoBreakTime + 1
            for i in range(x):
                print(convertTime(pomoBreakTime))
                if playPauseCheckB == False:
                    return
                pomoBreakTime = pomoBreakTime - 1
                time.sleep(1)
            inPomoBreak = False  # changes to work
         
        resetMode()
        print("Done with a cycle! Please press play button to start new cycle")
        playPauseCheckB = False
         
def resetMode(): # reset the values to default
    global pomoWorkTime
    global pomoBreakTime
    global taskNum
    global budgetTime
    global uTaskNum
    global uBudgetTime
    
    # reset to user input times
    pomoWorkTime = uPomoWTime
    pomoBreakTime = uPomoBTime
    taskNum = uTaskNum
    budgetTime = uBudgetTime
    

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
#     global pomoWorkTime
#     global pomoBreakTime
#     global taskNum
#     global budgetTime
#     risingCntUp = False
    
#     while True:
#         if readButton(pinB): # 1 button pressed, 0 button not pressed
#             if risingCntUp == False and settingMenu:
#                 risingCntUp = True
#                 if mode == 0:
#                     if pressedOnce == 1:
#                         pomoWorkTime+=300 # increment pomo time by 5 min
#                     elif pressedOnce == 2:
#                         pomoBreakTime+=300 # increment pomo break time by 5 min
#                 elif mode == 1:
#                     taskNum+=1 # increment tasks
#                 else:
#                     budgetTime+=300 # increment break time by 5 min
#         else:
#             risingCntUp = False        
            
# def countDn():  # count down
#     global mode
#     global settingMenu
#     global pressedOnce
#     global pomoWorkTime
#     global pomoBreakTime
#     global taskNum
#     global budgetTime
#     risingCntDn = False
    
#     while True:
#         if readButton(pinC): # 1 button pressed, 0 button not pressed
#             if risingCntDn == False and settingMenu:
#                 risingCntDn = True
#                 if mode == 0:
#                     if pressedOnce == 1:
#                         pomoWorkTime-=300 # decrement pomo time by 5 min
#                         if pomoWorkTime < 300:
#                             pomoWorkTime = 300
#                     elif pressedOnce == 2:
#                         pomoBreakTime-=300 # decrement pomo break time by 5 min
#                         if pomoBreakTime < 300:
#                             pomoBreakTime = 300
#                 elif mode == 1:
#                     if taskNum > 1:
#                         taskNum-=1 # decrement tasks
#                 else:
#                     budgetTime-=300 # decrement break time by 5 min
#                     if budgetTime < 300:
#                         budgetTime = 300
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
    time = str(hours).rjust(2,'0') + ':' + str(minutes).rjust(2,'0') + ':' + str(seconds).rjust(2,'0')
    return time
            
# def updateDisplay():
#     global settingsSaved
#     while True:
#         display.clear()
#         if settingsSaved == False:
#             if mode == 0:
#                 display.clear()
#                 if inPomoBreak:
#                     display.text("Break Time:", 25, 0, 12)
#                     display.text(convertTime(pomoBreakTime), 30, 10,25)
#                 else:
#                     display.text("Break Time:", 25, 0, 12)
#                     display.text(convertTime(pomoWorkTime), 30, 10,25)
#             elif mode == 1:
#                     display.text('Tasks:', 30, 0, 12)
#                     display.text(str(taskNum), 30, 10, 35) # will need to adjust axes

#             elif mode == 2:
#                     display.text("Break Time:", 25, 0, 12)
#                     display.text(convertTime(budgetTime), 30, 10,25)

#             display.show()        
#             time.sleep(1)
        
            
displayWelcome()
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

# t7 = Thread(target=updateDisplay)
# t7.start()

# t8 = Thread(target=Tree)
# t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
# t7.join()
# t8.join()
