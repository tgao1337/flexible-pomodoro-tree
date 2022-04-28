# This is the Flexible Pomodoro Tree official code
 
from threading import Thread, Event, Lock
from pomodoro import *
from multiprocessing import Process
import multiprocessing as mp

global mode
global state

mode = "POMODORO"
state = "WELCOME" # WELCOME, OVERVIEW, RUN, MODE_SELECT, MODE_SETTINGS

# dispLock=Lock()

resetBEvent = mp.Event()
playPauseCompleteBEvent = mp.Event()
settingsBEvent = mp.Event()
upBEvent = mp.Event()
downBEvent = mp.Event()


# ================================================ NEW CODE =======================================================

def checkResetB(): # PROCESS
    global resetBEvent
    while True:
        waitButton(pinB)
        resetBEvent.set()
      
def checkPlayPauseCompleteB(): # PROCESS
    global playPauseCompleteBEvent
    while True:
        waitButton(pinA)
        playPauseCompleteBEvent.set()

def checkSettingsB(): # PROCESS
    global settingsBEvent
    while True:
        waitButton(pinC)
        settingsBEvent.set()

def checkUpB(): # PROCESS
    global upBEvent
    while True:
        waitButton(pinD)
        upBEvent.set()
      
def checkDownB(): # PROCESS
    global downBEvent
    while True:
        waitButton(pinE)
        downBEvent.set()
      
def watchEvents(): # THREAD
    global resetBEvent
    global playPauseCompleteBEvent
    global settingsBEvent
    global upBEvent
    global downBEvent
    global state
    global mode
  
    while True:
        if resetBEvent.is_set():
            # change mode and state
            print("Reset Button was pressed")
            state = "WELCOME"
            resetBEvent.clear()
          
        if playPauseCompleteBEvent.is_set():
            print("Play Pause Complete Button was pressed")
            state = "RUN"
            playPauseCompleteBEvent.clear()
           
        if settingsBEvent.is_set():
            state = "MODE_SELECT"
            print("Settings Button was pressed")
            settingsBEvent.clear()
           
        if upBEvent.is_set():
            print("Up Button was pressed")
            if state = "MODE_SELECT":
                if mode == "TASK":
                    mode = "POMODORO"
                if mode == "BUDGET":
                    mode = "TASK"                
            upBEvent.clear()
           
        if downBEvent.is_set():
            print("Down Button was pressed")
            if state = "MODE_SELECT":
                if mode == "POMODORO":
                    mode = "TASK"
                if mode == "TASK":
                    mode = "BUDGET"   
          
            downBEvent.clear()
        time.sleep(0.01)
        
        
def updateDisplay():

    while True:
        if state == "WELCOME":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((43, 43), "Welcome", fill="white")
          
        if state == "OVERVIEW":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO":
                    draw.text((43, 43), "POM OVERVIEW", fill="white")
                if mode == "TASK":
                    draw.text((43, 43), "TASK OVERVIEW", fill="white")
                if mode == "BUDGET":
                    draw.text((43, 43), "BUDGET OVERVIEW", fill="white")
                 
        if state == "RUN":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO":
                    draw.text((43, 43), "POM RUN", fill="white")
                if mode == "TASK":
                    draw.text((43, 43), "TASK RUN", fill="white")
                if mode == "BUDGET":
                    draw.text((43, 43), "BUDGET RUN", fill="white")
                 
        if state == "MODE_SELECT":
            
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((30,45), "Select Mode", fill="white")
                draw.text((32,0), "Pomodoro", fill="white")
                draw.text((32,12), "Task", fill="white")
                draw.text((32,24), "Budget", fill="white")

                if mode == "POMODORO":
                    draw.text((20,0), ">", fill="white")
                if mode == "TASK":
                    draw.text((20,12), ">", fill="white")
                if mode == "BUDGET":
                    draw.text((20,24), ">", fill="white")
                
         
        if state == "MODE_SETTINGS":
            pass
            
         
        
    
      
      
# =================================================================================================================
    
'''

    

    
def checkUp(): #thread
    print("Running thread: CheckUp")
    global upButton
    global settingsButton
    debouncePinD = False
    while True:
        if readButton(pinD):
            if debouncePinD == False:
                debouncePinD = True
#                 if settingsButton:
                upButton = True
                print("Up Button Pressed")
#                 else: 
#                     upButton = False
        else:
            debouncePinD = False
    
def checkDown(): #thread
    print("Running thread: CheckDown")
    global downButton
    debouncePinE = False
    while True:
        if readButton(pinE):
            if debouncePinE == False:
                debouncePinE = True
#                 if settingsButton:
                downButton = True
                print("Down Button Pressed")
#                 else:
#                     downButton = False
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
              
#         print("playPauseCheckB:", playPauseCheckB, "settingsSaved:", settingsSaved, "resetRequired:", resetRequired)
        if playPauseCheckB and settingsSaved and resetRequired: # If the playPauseCheckB has been pressed and settingsSaved start Tree
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
#         while not resetRequired:
        print("Welcome! Press Start and Settings to select a mode")
#         display.clear()
# #         draw tree
#         display.draw_line(0, 45, 127 ,45)
#         display.text("Welcome", 40, 43, 12)
#         display.show()
        with canvas(device) as draw:
            draw.line((0, 45, 127 ,45), fill="white")
            draw.text((40, 43), "Welcome", fill="white")
   
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
                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n > Pomodoro \n    Task \n    Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("> Pomodoro \n  Task \n  Budget")
                      
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("> Pomodoro", 20,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("Budget", 32,24,14)
                with canvas(device) as draw:
                    draw.line((0, 45, 127 ,45), fill="white")
                    draw.text((30,45), "Select Mode", fill="white")
                    draw.text((20,0), "> Pomodoro", fill="white")
                    draw.text((32,12), "Task", fill="white")
                    draw.text((32,24), "Budget", fill="white")
 
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
                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n    Pomodoro \n > Task \n    Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("  Pomodoro \n> Task \n  Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("> Task", 20,12,14)
#                 display.text("Budget", 32,24,14)
                with canvas(device) as draw:
                    draw.line((0, 45, 127 ,45), fill="white")
                    draw.text((30,45), "Select Mode", fill="white")
                    draw.text((32,0), "Pomodoro", fill="white")
                    draw.text((20,12), "> Task", fill="white")
                    draw.text((32,24), "Budget", fill="white")
                
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
                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n    Pomodoro \n    Task \n > Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")            
                    print("  Pomodoro \n  Task \n> Budget")
#                 display.draw_line(0, 45, 127 ,45)
#                 display.text("Select Mode", 30,45,12)
#                 display.text("Pomodoro", 32,0,14)
#                 display.text("Task", 32,12,14)
#                 display.text("> Budget", 20,24,14)
                with canvas(device) as draw:
                    draw.line((0, 45, 127 ,45), fill="white")
                    draw.text((30,45), "Select Mode", fill="white")
                    draw.text((32,0), "Pomodoro", fill="white")
                    draw.text((32,12), "Task", fill="white")
                    draw.text((20,24), "> Budget", fill="white")
                
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
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((20,45), "P | Settings | 4", fill="white")
                draw.text((25, 0), "Set Work Time:", fill="white")
                draw.text((30, 10), convertTime(pomoWorkTime), fill="white")
            
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
#             display.text(convertTime(pomoBreakTime), 30, 10, 25)  # changed pomoWorkTime to pomoBreakTime
#             display.show()
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((20,45), "P | Settings | 4", fill="white")
                draw.text((20, 0), "Set Break Time:", fill="white")
                draw.text((30, 10), convertTime(pomoBreakTime), fill="white")
   
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
             with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((35,45), "T | Settings", fill="white")
                draw.text((40, 0), "Set Tasks:", fill="white")
             # display.clear()
             # display.draw_line(0, 45, 127 ,45)
             # display.text("T | Settings", 35,45,12)
             # display.text("Set Tasks:", 40, 0, 12)
                if taskNum > 9:
                    draw.text((50, 10), str(taskNum), fill="white")
                   # display.text(str(taskNum), 50, 10, 25)
                else:
                    draw.text((60, 10), str(taskNum), fill="white")
                    # display.text(str(taskNum), 60, 10, 25)
             # display.show()  
             
             
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
  
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((35,45), "B | Settings", fill="white")
                draw.text((20, 0), "Set Break Time:", fill="white")
                draw.text((30, 10), convertTime(budgetTime), fill="white")
    settingsButton = False
    uBudgetTime = budgetTime
    settingsSaved = True


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
            # display.clear()
            # display.text('Flexible Pomodoro Tree', 6, 0)
            # display.text('Settings OK ? Press play -->', 12 ,0)
            # display.text( 'NO ? press settings', 14, 0)
            # display.text('Study ' + convertTime(pomoWorkTime), 20, 0)
            # display.text('Break ' + convertTime(pomoBreakTime), 24,0)
            with canvas(device) as draw:
                draw.text((6, 0), "Flexible Pomodoro Tree", fill="white")
                draw.text((12, 0), "Settings OK ? Press play -->", fill="white")
                draw.text((14, 0), "NO ? press settings", fill="white")
                draw.text((20, 0), "Study: "+convertTime(pomoWorkTime), fill="white")
                draw.text((24,0), "Break: "+convertTime(pomoBreakTime), fill="white")
        if mode ==1:
            # display.clear()
            # display.text('Flexible Pomodoro Tree', 6, 0)
            # display.text('Settings OK ? Press play -->', 12 ,0)
            # display.text( 'NO ? press settings', 14, 0)
            # display.text('# tasks' + str(taskNum), 20, 0)
            with canvas(device) as draw:
                draw.text((6, 0), "Flexible Pomodoro Tree", fill="white")
                draw.text((12, 0), "Settings OK ? Press play -->", fill="white")
                draw.text((14, 0), "NO ? press settings", fill="white")
                draw.text((20, 0), '# tasks: ' + str(taskNum), fill="white")
        if mode==2:  
            # display.clear()
            # display.text('Flexible Pomodoro Tree', 6, 0)
            # display.text('Settings OK ? Press play -->', 12 ,0)
            # display.text( 'NO ? press settings', 14, 0)
            # display.text('Total break time' + convertTime(budgetTime), 20, 0)
            with canvas(device) as draw:
                draw.text((6, 0), "Flexible Pomodoro Tree", fill="white")
                draw.text((12, 0), "Settings OK ? Press play -->", fill="white")
                draw.text((14, 0), "NO ? press settings", fill="white")
                draw.text((20, 0), 'Total break time: ' + convertTime(budgetTime), fill="white")
             
        # display.show()
        
    while True:
        if playPauseCheckB:
            playPauseCheckB = False
            return True
        if settingsButton:
            settingsButton = False
            return False

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
    global playPauseCheckB
    
    if playPauseCheckB:
        if not inPomoBreak:
            print("Mode: Pomodoro, Work")
            x = pomoWorkTime + 1
            
            for i in range(x):
                if playPauseCheckB == False or resetRequired == False:
                    return
                print(convertTime(pomoWorkTime))
                pomoWorkTime = pomoWorkTime - 1
                time.sleep(1)
            inPomoBreak = True  # changes to break
            
        if inPomoBreak:
            print("Mode: Pomodoro, Break")
            x = pomoBreakTime + 1
            for i in range(x):
                if playPauseCheckB == False or resetRequired == False:
                    return
                print(convertTime(pomoBreakTime))
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
        
'''    



p1 = Process(target=checkResetB)
p1.start()
p2 = Process(target=checkPlayPauseCompleteB)
p2.start()
p3 = Process(target=checkSettingsB)
p3.start()
p4 = Process(target=checkUpB)
p4.start()
p5 = Process(target=checkDownB)
p5.start()

t1 = Thread(target=watchEvents)
t1.start()
t2 = Thread(target=updateDisplay)
t2.start()

t1.join()
t2.join()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()


