# This is the Flexible Pomodoro Tree official code
 
from threading import Thread, Event, Lock
from pomodoro import *
from multiprocessing import Process
import multiprocessing as mp

global mode
global state
global pomoWorkTime
global pomoBreakTime
global taskDone
global taskNum
global budgetTime
global displayTime
global prodTime
global prevState
global quantityON
global timeTillNextLed
global prodTime
global settingsChanged
# global endTime

mode = "POMODORO_W" # POMODORO_W, POMODORO_B, TASK, BUDGET
state = "WELCOME" # WELCOME, OVERVIEW, RUN, PAUSE, MODE_SELECT, MODE_SETTINGS, MODE_SETTINGS_2 (For Pomodoro Break Settings)

pomoWorkTime = 0.5 * 60  # These are default values  # TODO FIX because using testing values for now
pomoBreakTime = 0.25 * 60  # These are default values
taskDone = 0
taskNum = 4  # these are default values
budgetTime = 0.25 * 60  # these are default values
prodTime = 0
settingsChanged = False

startTime = 0
endTime = 0
x = time.gmtime(pomoWorkTime)
displayTime = time.strftime("%H:%M:%S", x)
prevState = None
quantityON = 0
timeTillNextLed=60

resetBEvent = mp.Event()
playPauseCompleteBEvent = mp.Event()
settingsBEvent = mp.Event()
upBEvent = mp.Event()
downBEvent = mp.Event()
pomoRunEvent = mp.Event()

buttonSetup()
setupLED()
clearAll()
buzzerSetup(13)



# ================================================ NEW CODE =======================================================

# reading and writing settings to file? or can i use pickle?
# pickle may be easier with a struct of all settings then load it in later.
# for file, need to edit strings and then rewrite file every time
# f = open("settings.txt", "w+")



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
      
def pomoRun(): 
    global displayTime
    global prodTime
    global mode
    global state
    global prevState
    global timeTillNextLed
    prevTimeTillNex = 0
    timeElapsed = 0
    global settingsChanged
    
    
    while True:
        prevTimeTillNex = timeTillNextLed
        if state == "MODE_SETTINGS_2":
            startTime = time.time()
            endTime = startTime + pomoBreakTime
            timeLeft = pomoBreakTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
       
        if state == "MODE_SETTINGS" and (mode == "POMODORO_W" or mode == "POMODORO_B"):
            print("Hello i am in here")
            startTime = time.time()
            endTime = startTime + pomoWorkTime
            timeLeft = pomoWorkTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            
        if state == "MODE_SETTINGS" and mode == "BUDGET":
            startTime = time.time()
            endTime = startTime + budgetTime
            timeLeft = budgetTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
       
       
       
        if state == "PAUSE":
            prevState = "PAUSE"
            startTime = time.time()
            if mode == "POMODORO_W":
                endTime = startTime + pomoWorkTime
                timeLeft = pomoWorkTime
            elif mode == "POMODORO_B":
                endTime = startTime + pomoBreakTime
                timeLeft = pomoBreakTime
               
            elif mode == "BUDGET":
                endTime = startTime + budgetTime
                timeLeft = budgetTime
               
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            
            
        if state == "RUN" and mode == "BUDGET":
            prevState = "PAUSE"
            startTime = time.time()
            endTime = startTime + budgetTime
            timeLeft = budgetTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
        
        # ========================================================================
        
        if state == "RUN" and mode == "POMODORO_W":
         
            prevState = "RUN"
            startTime = time.time()
            endTime = startTime + pomoWorkTime
            timeLeft = pomoWorkTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            
            while time.time() <= endTime and mode == "POMODORO_W":

                if state == "MODE_SELECT" or state == "MODE_SETTINGS" or state == "MODE_SETTINGS_2":
                    
                    
                    if settingsChanged:
                        settingsChanged = False
#                         startTime = endTime - pomoWorkTime
                        timeElapsed = time.time() - startTime
                        timeLeft = pomoWorkTime - timeElapsed
                        endTime = time.time() + timeLeft


                        x = time.gmtime(timeLeft)
    #                     print("CHANGES MADE:", time.strftime("%H:%M:%S", x), startTime, timeLeft, endTime, timeElapsed)
                        a = time.gmtime(startTime)
                        b = time.gmtime(endTime)
                        c = time.gmtime(timeElapsed)
                        d = time.gmtime(time.time())
                        print("CHANGES MADE:", time.strftime("%H:%M:%S", x),time.strftime("%H:%M:%S", d),  time.strftime("%H:%M:%S", a), time.strftime("%H:%M:%S", b), time.strftime("%H:%M:%S", c))

                        timeTillNextLed = timeLeft // getAvailable()
                        prevTimeTillNex = timeTillNextLed
    #                     print("CHANGES MADE:", timeTillNextLed, startTime, timeLeft, prevTimeTillNex, getAvailable())

                    

             
                elif state == "RUN" or (prevState == "RUN" and not state=="RUN" and not state == "PAUSE"):
                    timeLeft = endTime - time.time()
                    print("----->", (time.time() - startTime), timeTillNextLed, prevTimeTillNex, getAvailable())
                    if ((time.time() - startTime) > timeTillNextLed):
#                     if (timeElapsed > timeTillNextLed):
                        timeTillNextLed = timeTillNextLed + prevTimeTillNex 
                        toggleNextLed(True,1)
                        print("LED TURNED ON")

                    
                    x = time.gmtime(timeLeft)
                    prevState = "RUN"
                    
                if state == "PAUSE" or (prevState == "PAUSE" and not state=="RUN" and not state == "PAUSE"):
                    endTime = time.time() + timeLeft
                    prevState = "PAUSE"
                    startTime = endTime - pomoWorkTime
                      
                displayTime = time.strftime("%H:%M:%S", x)
#                 print("current time:", displayTime)
                
            
            if mode == "POMODORO_W":
                mode = "POMODORO_B"
                state = "PAUSE"
                x = time.gmtime(pomoBreakTime)
                displayTime = time.strftime("%H:%M:%S", x)
            
        if state == "RUN" and mode == "POMODORO_B":
            prevState = "RUN"
            startTime = time.time()
            endTime = startTime + pomoBreakTime
            timeLeft = pomoBreakTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            while time.time() <= endTime and mode == "POMODORO_B":
                if settingsChanged:
                    timeElapsed = time.time() - startTime
                    timeLeft = pomoWorkTime - timeElapsed
                    endTime = time.time() + timeLeft


                    x = time.gmtime(timeLeft)

                    settingsChanged = False
                    
                if state == "RUN" or (prevState == "RUN" and not state=="RUN" and not state == "PAUSE"):
                    timeLeft = endTime - time.time()
                    x = time.gmtime(timeLeft)
                    prevState = "RUN"
                    
                if state == "PAUSE" or (prevState == "PAUSE" and not state=="RUN" and not state == "PAUSE"):
                    endTime = time.time() + timeLeft
                    prevState = "PAUSE"
                displayTime = time.strftime("%H:%M:%S", x)
                
            if mode == "POMODORO_B":
                mode = "POMODORO_W"
                state = "PAUSE"
                x = time.gmtime(pomoWorkTime)
                displayTime = time.strftime("%H:%M:%S", x)
            
        if state == "RUN" and mode == "BUDGET":   # show productivity time on budget
            # prevState = "PAUSE"
            productivity_time=0
            timeTillNextLed = 21600 // available_led # 6 hour work time like wesaid
           
            startTime = time.time()
            endTime = startTime + budgetTime
            timeLeft = budgetTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            y = time.gmtime(timeLeft)
            prodTime = time.strftime("%H:%M:%S", y)
            while time.time() <= endTime and mode == "BUDGET":
                if state == "RUN" or (prevState == "RUN" and not state=="RUN" and not state == "PAUSE"):
                    endTime = time.time() + timeLeft
                    productivity_time = time.time()- startTime
                    y = time.gmtime(productivity_time)
                    if productivity_time > timeTillNextLed: # turn on led when not in break
                        timeTillNextLed += timeTillNextLed
                        toggleNextLed(True,1)
                    prevState = "RUN"
                if state == "PAUSE" or (prevState == "PAUSE" and not state=="RUN" and not state == "PAUSE"):
                    timeLeft = endTime - time.time()
                    
                    startTime=time.time()- productivity_time
                    
                    x = time.gmtime(timeLeft)
                    prevState = "PAUSE"
                prodTime = time.strftime("%H:%M:%S", y)  # productivity time to display on OLED
                displayTime = time.strftime("%H:%M:%S", x)   # if budget mode done then go to pomodoro, shows budget time, this will fix if displayTime = pomodorotime in start of pomodoro loop
                  
      
def watchEvents(): # THREAD
    global resetBEvent
    global playPauseCompleteBEvent
    global settingsBEvent
    global upBEvent
    global downBEvent
    global state
    global mode
    global displayTime
    global taskDone
    global prevState
    global taskDone
    global taskNum
    global pomoWorkTime
    global pomoBreakTime
    global budgetTime
    global quantityON
    global timeTillNextLed
    global settingsChanged

    while True:

        
        if resetBEvent.is_set():
            # change mode and state
            print("Reset Button was pressed")
            if state == "WELCOME":
                f = open("userSettings.txt", "r")
                mode = f.readline()[:-1]
                if mode == "POMODORO_B":
                    mode = "POMODORO_W"
                pomoWorkTime = int(f.readline()[:-1])
                pomoBreakTime = int(f.readline()[:-1])
                taskNum = int(f.readline()[:-1])
                budgetTime = int(f.readline()[:-1])
                taskDone = 0
                f.close()
                clearAll()
                state = "OVERVIEW"
                
                resetAvailable()  # resetting available_leds back to 32
                quantityON = NUM_LEDS // taskNum
                  
                timeTillNextLed = pomoWorkTime // NUM_LEDS
                print("timeTillNextLed in reset:", timeTillNextLed)

            
            
            else:
                state = "WELCOME"
                # TODO: RESET VALUES/TIME STUFF FROM FILE??
                f = open("userSettings.txt", "w")
                f.write(mode+"\n")
                f.write((str(pomoWorkTime)+"\n"))
                f.write((str(pomoBreakTime)+"\n"))
                f.write((str(taskNum)+"\n"))
                f.write((str(budgetTime)+"\n"))
                f.close()

            resetBEvent.clear()
          
        if playPauseCompleteBEvent.is_set():
            print("Play Pause Complete Button was pressed")
            if state == "RUN" and not mode == "TASK":
                state = "PAUSE"
            
            elif state == "PAUSE" and not mode == "TASK":
                state = "RUN"
              
            elif state == "MODE_SELECT" or state == "OVERVIEW" or state == "MODE_SETTINGS" or state == "MODE_SETTINGS_2":
                if (mode == "BUDGET" or mode == "POMODORO_W" or mode == "POMODORO_B") and not prevState == None:
                    state = prevState  # this will put it back in the previous mode
                else: 
                    if mode == "TASK":
                        taskDone = taskDone - 1
                        toggleNextLed(False, quantityON)
                    state = "RUN"
                
            if mode == "TASK":
                if (taskDone >= taskNum):
                    state = "WELCOME"
                    buzzUp3()
                else:
                    taskDone = taskDone + 1
                    remainingTasks = taskNum - taskDone
                    buzzUp2()
                    if remainingTasks == 0:
                        allOn()
                    else:
                        print("Quantity on:", quantityON)
                        if taskDone >=1:
                            toggleNextLed(True, quantityON)
                            print("AVAILABLE LEDS NOW:", getAvailable())

            
            playPauseCompleteBEvent.clear()
           
        if settingsBEvent.is_set():
            if state == "WELCOME" or state == "OVERVIEW" or state == "MODE_SETTINGS_2" or state == "RUN" or state == "PAUSE":
                state = "MODE_SELECT"
            elif state == "MODE_SELECT":
                state = "MODE_SETTINGS"
            elif state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    state = "MODE_SETTINGS_2"
                else:
                    state = "MODE_SELECT"
                  
            print("Settings Button was pressed")
            settingsBEvent.clear()
           
        if upBEvent.is_set():
            print("Up Button was pressed")
            if state == "MODE_SELECT":
                if mode == "TASK":
                    mode = "POMODORO_W"
                elif mode == "BUDGET":
                    mode = "TASK"
                    
                   
                  
            if state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoWorkTime < 7200:
                        pomoWorkTime += 300
                        settingsChanged = True
                   
                        timeTillNextLed = pomoWorkTime // getAvailable()
                    
                        print("----->", timeTillNextLed, pomoWorkTime, getAvailable())
                  
                if mode == "TASK":
                    if taskNum < 32: #upper limit 100 tasks
                        taskNum += 1
                        quantityON = getAvailable() // taskNum
                        print("----->", quantityON, getAvailable(), taskNum)

                if mode == "BUDGET":
                    if budgetTime < 18000:
                        budgetTime += 600
                  
            if state == "MODE_SETTINGS_2":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoBreakTime < 3600:
                        pomoBreakTime += 300
                        settingsChanged = True
            
            upBEvent.clear()
           
        if downBEvent.is_set():
            print("Down Button was pressed")
            if state == "MODE_SELECT":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    mode = "TASK"


                elif mode == "TASK":
                    mode = "BUDGET"

            if state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoWorkTime >= 600:
                        pomoWorkTime -= 300
                        settingsChanged = True
#                         endTime -= 300
                        timeTillNextLed = pomoWorkTime // getAvailable()
                        print("----->", timeTillNextLed, pomoWorkTime, getAvailable())
                  
                if mode == "TASK":
                    if taskNum > 1:
                        taskNum -= 1
                        quantityON = getAvailable() // taskNum
                        print("----->", quantityON, getAvailable(), taskNum)

                if mode == "BUDGET":
                    if budgetTime > 600:
                        budgetTime -= 600
                  
            if state == "MODE_SETTINGS_2":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoBreakTime > 300:
                        pomoBreakTime -= 300
                        settingsChanged = True
                  
                  

            downBEvent.clear()
        time.sleep(0.01)
        
        
def updateDisplay():

    while True:
        if state == "WELCOME":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((40, 43), "Welcome", font=fontSmall, fill="white")
          
        if state == "OVERVIEW":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((38, 43), "OVERVIEW", font=fontSmall, fill="white")
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    x = time.gmtime(pomoWorkTime)
                    displayWorkTime = time.strftime("%H:%M:%S", x)
                    y = time.gmtime(pomoBreakTime)
                    displayBreakTime = time.strftime("%H:%M:%S", y)
                    draw.text((13,0), "Mode: Pomodoro", font=fontSmall, fill="white")
                    draw.text((5,14), "Work Time: "+displayWorkTime, font=fontSmall, fill="white")
                    draw.text((5,28), "Break Time: "+displayBreakTime, font=fontSmall, fill="white")

                if mode == "TASK":
                    draw.text((31,0), "Mode: Task", font=fontSmall, fill="white")
                    draw.text((25,20), "Total Tasks: " + str(taskNum), font=fontSmall, fill="white")
                if mode == "BUDGET":
                    x = time.gmtime(budgetTime)
                    displayBudTime = time.strftime("%H:%M:%S", x)
                    draw.text((21,0), "Mode: Budget", font=fontSmall, fill="white")
                    draw.text((0,20), "Budget Time: "+displayBudTime, font=fontSmall, fill="white")
                 
        if state == "RUN":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                  
                if mode == "POMODORO_W":
                    draw.text((38,45), "P | Work", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white")
                elif mode == "POMODORO_B":
                    draw.text((31,45), "P | Break", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white")

                if mode == "TASK":
                    taskString = str(taskDone) + "/" + str(taskNum)
                    draw.text((17, 10), taskString, font=fontBig, fill="white")
                    draw.text((31,45), "T | Task", font=fontSmall, fill="white")  # TODO add task name
                if mode == "BUDGET":
                    draw.text((18,0), "Productive time:", font=fontSmall, fill="white")
                    draw.text((17,10), prodTime, font=fontBig, fill="white")  # productivity time  TODO YOU NEED TO FIX THIS
                    draw.text((12,45), "B | Budget | Work", font=fontSmall, fill="white")

                  
                  
        if state == "PAUSE":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                  
                if mode == "POMODORO_W":
                    draw.text((15,45), "P | Work | Paused", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white")
                elif mode == "POMODORO_B":
                    draw.text((11,45), "P | Break | Paused", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white")
                   
                if mode == "TASK":
                    taskString = str(taskDone) + "/" + str(taskNum)
                    draw.text((17, 10), taskString, font=fontBig, fill="white")
                    draw.text((31,45), "T | Task", font=fontSmall, fill="white")  # TODO add task name
                if mode == "BUDGET":
                    draw.text((0,0), "Break time remaining:", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white")  # change position to display
                    draw.text((12,45), "B | Budget | Break", font=fontSmall, fill="white")  # TODO add productivity time

                   
                   
                   
                 
        if state == "MODE_SELECT":
            
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((30,45), "Select Mode", font=fontSmall, fill="white")
                draw.text((32,0), "Pomodoro", font=fontSmall, fill="white")
                draw.text((32,12), "Task", font=fontSmall, fill="white")
                draw.text((32,24), "Budget", font=fontSmall, fill="white")

                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    draw.text((20,0), ">", font=fontSmall, fill="white")
                if mode == "TASK":
                    draw.text((20,12), ">", font=fontSmall, fill="white")
                if mode == "BUDGET":
                    draw.text((20,24), ">", font=fontSmall, fill="white")
                
         
        if state == "MODE_SETTINGS":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    draw.text((15,45), "P | Settings | "+ displayTime, font=fontSmall, fill="white")  # Removed cycles  # TODO do i add time to this while it's still playing?
                    draw.text((23, 0), "Set Work Time:", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white") #TODO Timing conversion printing
                if mode == "TASK":
                    draw.text((31,45), "T | Settings", font=fontSmall, fill="white")
                    draw.text((40, 0), "Set Tasks:", font=fontSmall, fill="white")
                    if taskNum > 9:
                        draw.text((50, 10), str(taskNum), font=fontBig, fill="white") #TODO Task count manager
                    else:
                        draw.text((60, 10), str(taskNum), font=fontBig, fill="white") #TODO Task count manager
                if mode == "BUDGET":
                    draw.text((0,45), "B | Settings | "+ displayTime, font=fontSmall, fill="white")  # TODO do i add time to this while it's still playing?
                    draw.text((23, 0), "Set Break Time:", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white") # TODO Budget break timing
                
        if state == "MODE_SETTINGS_2":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    draw.text((31,45), "P | Settings | "+displayTime, font=fontSmall, fill="white")  # Removed cycles
                    draw.text((23, 0), "Set Break Time:", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white") #TODO Timing conversion printing
            
           


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
t3 = Thread(target = pomoRun)
t3.start()

t1.join()
t2.join()
t3.join()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()


