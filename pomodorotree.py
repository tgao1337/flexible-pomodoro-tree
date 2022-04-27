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

def buzzUp():
    playList([(C4, 0.25), (E4, 0.25), (G4, 0.25), (C5, 0.25)])

def buzzDown():
    playList([(C5, 0.25), (G4, 0.25), (E4, 0.25), (C4, 0.25)])

def checkReset(): # Done for day button
    global resetRequired
    global settingsSaved 

    while True:
        waitButton(pinB)
        time.sleep(0.2)
        resetRequired = not resetRequired
        
        if resetRequired:
            print("Start for the day. resetRequired:", resetRequired)
            resetMode()
            settingsSaved = False
        else:
            print("End for the day. resetRequired:", resetRequired)
          
def checkPlayPauseComplete(): # Play pause check
    global playPauseCheckB
    while True:
        waitButton(pinA)
        playPauseCheckB = not playPauseCheckB
        print("PlayPauseComplete Button Pressed. playPauseCheckB:", playPauseCheckB)

def checkSettings():
    global settingsButton 
    while True:
        waitButton(pinC)
        settingsButton = True      
        print("Settings Button Pressed. settingsButton:", settingsButton)

def checkUp():
    global upButton
    global settingsButton
    while True:
        waitButton(pinD)
        upButton = True
        print("Up Button Pressed. upButton:", upButton)
    
def checkDown():
    global downButton
    while True:
        waitButton(pinE)
        downButton = True
        print("Down Button Pressed. downButton:", downButton)

    
def logic():
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
              
        if playPauseCheckB and settingsSaved and resetRequired: # If the playPauseCheckB has been pressed and settingsSaved start Tree
            if mode == 0:
                startPomodoro()
                print("Starting Pomodoro now!")
            elif mode == 1:
                startTask()
            elif mode == 2:
                startBudget()
           
            
def displayWelcome():
    with dispLock:
#         while not resetRequired:
        print("Welcome! Press Start and Settings to select a mode")
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
                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n > Pomodoro \n    Task \n    Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("> Pomodoro \n  Task \n  Budget")
                      
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
                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n    Pomodoro \n > Task \n    Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")
                    print("  Pomodoro \n> Task \n  Budget")

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

                with canvas(device) as draw:
                    draw.text((20, 0), "Select Mode:\n    Pomodoro \n    Task \n > Budget", fill="white")
                if modeChangeDetected:
                    modeChangeDetected = False
                    print("==========")            
                    print("  Pomodoro \n  Task \n> Budget")

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
                
                if taskNum > 9:
                    draw.text((50, 10), str(taskNum), fill="white")
                else:
                    draw.text((60, 10), str(taskNum), fill="white")
             
             
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

# t2 = Thread(target=checkPlayPauseComplete)
# t2.start()

# t3 = Thread(target=checkSettings)
# t3.start()

# t4 = Thread(target=checkUp)
# t4.start()

# t5 = Thread(target=checkDown)
# t5.start()

# t6 = Thread(target=logic)
# t6.start()

# t7 = Thread(target=updateDisplay)
# t7.start()

# t8 = Thread(target=Tree)
# t8.start()

t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
