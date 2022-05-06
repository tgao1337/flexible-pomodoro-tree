from threading import Thread, Event, Lock
from pomodoro import *
from multiprocessing import Process
import multiprocessing as mp
from queue import Queue
from flask import Flask, render_template, redirect, request

# ========================================================

tree = Image.open("tree.png").resize((32,32)).convert("1")

global mode, state, pomoWorkTime, pomoBreakTime, taskNum, taskDone, budgetTime
global displayTime, prodTime, quantityON, timeTillNextLed
global prevState

mode = "POMODORO_W" # POMODORO_W, POMODORO_B, TASK, BUDGET
state = "WELCOME" # WELCOME, OVERVIEW, RUN, PAUSE, MODE_SELECT, MODE_SETTINGS, MODE_SETTINGS_2 (For Pomodoro Break Settings)

pomoWorkTime = 25 * 60 # 25 minutes of work, starting pomoWorkTime
pomoBreakTime = 5 * 60 # 5 minutes of break, starting pomoBreakTime
taskNum = 4 # 4 total tasks
taskDone = 0 # Number of tasks completed
budgetTime = 2 * 60 * 60  # 2 hours of break / day
prodTime = 0 # Total produtivity time for budget mode. Must be >= budgetTime

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

queuePom = Queue()
queueBudget = Queue()

buttonSetup()
setupLED()
clearAll()
buzzerSetup(13)

# ============================ READ/WRITE USER SETTINGS ============================
def readSettings():
    global mode, pomoWorkTime, pomoBreakTime, taskNum, budgetTime
    userFile = open("userSettings.txt", "r")
    mode = userFile.readline()[:-1]
    if mode == "POMODORO_B":
        mode = "POMODORO_W"
    pomoWorkTime = int(userFile.readline())
    pomoBreakTime = int(userFile.readline())
    taskNum = int(userFile.readline())
    budgetTime = int(userFile.readline())
    userFile.close()
 
def writeSettings():
    userFile = open("userSettings.txt", "w")
    userFile.write(mode+"\n")
    userFile.write((str(pomoWorkTime)+"\n"))
    userFile.write((str(pomoBreakTime)+"\n"))
    userFile.write((str(taskNum)+"\n"))
    userFile.write((str(budgetTime)+"\n"))
    userFile.close()
 
# ============================ BUTTON PROCESS ============================
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
      
# ============================ TREE EXECUTION ============================
def runTree(): 
    global displayTime, prodTime, mode, state, prevState, timeTillNextLed
    prevTimeTillNextLed = 0
    timeElapsed = 0
    startPause = 0
    startRun = 0
    
    while True:
        prevTimeTillNextLed = timeTillNextLed
        if state == "MODE_SETTINGS_2":
            startTime = time.time()
            endTime = startTime + pomoBreakTime
            timeLeft = pomoBreakTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
       
        if state == "MODE_SETTINGS" and (mode == "POMODORO_W" or mode == "POMODORO_B"):
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
        
        # ============================== RUN/PAUSE POMODORO, BUDGET ==========================================
        
        if state == "RUN" and mode == "POMODORO_W":
            clearAll() # Reset LEDs
            prevState = "RUN"
            endTime = time.time() + pomoWorkTime
            timeLeft = pomoWorkTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            startRun = time.time()

            while time.time() <= endTime and mode == "POMODORO_W" and not state == "WELCOME":
                while not queuePom.empty():
                    endTime = endTime + queuePom.get()
                    timeLeft = endTime - time.time() 

#                 print((pomoWorkTime - timeLeft), timeTillNextLed)
                if state == "RUN" or (prevState == "RUN" and not state == "PAUSE"):
                    prevState = "RUN"
                    timeLeft = endTime - time.time() 
                    startPause = time.time()
                    
                    # LED TIMING
                    if ((pomoWorkTime - timeLeft) > timeTillNextLed):
                        timeTillNextLed = timeTillNextLed + prevTimeTillNextLed 
                        toggleNextLed(True,1)
                    
                if state == "PAUSE" or (prevState == "PAUSE" and not state == "RUN"): 
                    prevState = "PAUSE"
                    endTime = time.time() + timeLeft

                x = time.gmtime(timeLeft)
                displayTime = time.strftime("%H:%M:%S", x)
                    
            
            if mode == "POMODORO_W" and not state == "WELCOME":
                allOn()
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
            
            while time.time() <= endTime and mode == "POMODORO_B" and not state == "WELCOME":
                
                while not queuePom.empty():
                    endTime = endTime + queuePom.get()
                
                if state == "RUN" or (prevState == "RUN" and not state == "PAUSE"):
                    prevState = "RUN"
                    timeLeft = endTime - time.time() 
                    startPause = time.time()
                    
                if state == "PAUSE" or (prevState == "PAUSE" and not state == "RUN"): 
                    prevState = "PAUSE"
                    endTime = time.time() + timeLeft

                x = time.gmtime(timeLeft)
                displayTime = time.strftime("%H:%M:%S", x)
                
            if mode == "POMODORO_B"  and not state == "WELCOME":
                mode = "POMODORO_W"
                state = "PAUSE"
                x = time.gmtime(pomoWorkTime)
                displayTime = time.strftime("%H:%M:%S", x)
            
        if state == "RUN" and mode == "BUDGET":   # show productivity time on budget
            prevState = "RUN"
            productivity_time = 0
            timeTillNextLed = 21600 // available_led # 6 hour work time like wesaid
           
            startTime = time.time()
            endTime = startTime + budgetTime
            timeLeft = budgetTime
            x = time.gmtime(timeLeft)
            displayTime = time.strftime("%H:%M:%S", x)
            y = time.gmtime(timeLeft)
            prodTime = time.strftime("%H:%M:%S", y)
            
            while time.time() <= endTime and mode == "BUDGET" and not state == "WELCOME":
                
                while not queueBudget.empty():

                    endTime = endTime + queueBudget.get()
                    timeLeft = round(endTime - time.time())
                    print("New time left:", timeLeft)

                
                if state == "RUN" or (prevState == "RUN" and not state=="RUN" and not state == "PAUSE"): 
                    endTime = time.time() + timeLeft
                    productivity_time = time.time() - startTime
                    y = time.gmtime(productivity_time)
                  
                    if productivity_time > timeTillNextLed: # turn on led when not in break
                        timeTillNextLed += timeTillNextLed
                        toggleNextLed(True,1)
                    prevState = "RUN"
                    
                if state == "PAUSE" or (prevState == "PAUSE" and not state=="RUN" and not state == "PAUSE"):
                    timeLeft = endTime - time.time()
                    
                    startTime = time.time() - productivity_time
                    

                    prevState = "PAUSE"
                x = time.gmtime(timeLeft)
                prodTime = time.strftime("%H:%M:%S", y)  # productivity time to display on OLED
                displayTime = time.strftime("%H:%M:%S", x)   # if budget mode done then go to pomodoro, shows budget time, this will fix if displayTime = pomodorotime in start of pomodoro loop
                  
# ============================ WATCH BUTTON PRESSES ============================
def watchEvents(): # THREAD
    global resetBEvent, playPauseCompleteBEvent, settingsBEvent, upBEvent, downBEvent
    global state, mode, displayTime, pomoWorkTime, pomoBreakTime, taskNum, taskDone, budgetTime,  prevState
    global quantityON, timeTillNextLed

    while True:
        if resetBEvent.is_set():
            if state == "WELCOME":
                readSettings() # Read user settings
                clearAll() # Reset LEDs
                state = "OVERVIEW"   
                taskDone = 0
                resetAvailableLED()  # Resetting available_leds back to 32 in pomodoro.py
                quantityON = NUM_LEDS // taskNum # Calculate the number of LEDs to be on per Task
                timeTillNextLed = pomoWorkTime // NUM_LEDS # # Calculate the number of LEDs to be on every timeTillNextLed seconds

            else:
                state = "WELCOME"
                writeSettings() # Store current user settings to file

            resetBEvent.clear()
          
        if playPauseCompleteBEvent.is_set():
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
#                     buzzUp3()
                else:
                    taskDone = taskDone + 1
                    remainingTasks = taskNum - taskDone
#                     buzzUp2()
                    if remainingTasks == 0:
                        allOn()
                    else:
                        if taskDone >=1:
                            toggleNextLed(True, quantityON)
            playPauseCompleteBEvent.clear()
           
        if settingsBEvent.is_set():
#             if state == "WELCOME" or state == "OVERVIEW" or state == "MODE_SETTINGS_2" or state == "RUN" or state == "PAUSE":
            if state == "OVERVIEW" or state == "MODE_SETTINGS_2" or state == "RUN" or state == "PAUSE":
                state = "MODE_SELECT"
            elif state == "MODE_SELECT":
                state = "MODE_SETTINGS"
            elif state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    state = "MODE_SETTINGS_2"
                else:
                    state = "MODE_SELECT"
            settingsBEvent.clear()
           
        if upBEvent.is_set():
            # Swtiching modes
            if state == "MODE_SELECT":
                if mode == "TASK":
                    mode = "POMODORO_W"
                elif mode == "BUDGET":
                    mode = "TASK"
                    taskDone = 0

            # Changing settings       
            if state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoWorkTime < 7200:
                        pomoWorkTime += 300
                        queuePom.put(300)
                   
                        timeTillNextLed = pomoWorkTime // getAvailable() # Calculate new LED time
#                         print("----->", timeTillNextLed, pomoWorkTime, getAvailable())
                  
                if mode == "TASK":
                    if taskNum < 32: # Max 32 tasks because 32 LEDs
                        taskNum += 1
                        quantityON = getAvailable() // taskNum

                if mode == "BUDGET":
                    if budgetTime < 18000:
                        budgetTime += 600
                        queueBudget.put(600)

                writeSettings()
                  
            if state == "MODE_SETTINGS_2":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoBreakTime < 3600:
                        pomoBreakTime += 300
                        queuePom.put(300)
                writeSettings()
            upBEvent.clear()
           
        if downBEvent.is_set():
            # Switching modes
            if state == "MODE_SELECT":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    mode = "TASK"
                    taskDone = 0
                elif mode == "TASK":
                    mode = "BUDGET"
                    
            # Changing settings
            if state == "MODE_SETTINGS":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoWorkTime >= 600:
                        pomoWorkTime -= 300
                        queuePom.put(-300)
                        timeTillNextLed = pomoWorkTime // getAvailable()
#                         print("----->", timeTillNextLed, pomoWorkTime, getAvailable())
                  
                if mode == "TASK":
                    if taskNum > 1:
                        taskNum -= 1
                        quantityON = getAvailable() // taskNum
#                         print("----->", quantityON, getAvailable(), taskNum)

                if mode == "BUDGET":
                    if budgetTime > 600:
                        budgetTime -= 600
                        queueBudget.put(-600)
                writeSettings()
                
            if state == "MODE_SETTINGS_2":
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    if pomoBreakTime > 300:
                        pomoBreakTime -= 300
                        queuePom.put(-300)
                writeSettings()
            downBEvent.clear()
        time.sleep(0.01)
        
# ============================ UPDATE DISPLAY BASED ON CURRENT STATE AND MODE ============================
def updateDisplay():

    while True:
        if state == "WELCOME":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                draw.text((40, 43), "Welcome", font=fontSmall, fill="white")
                draw.bitmap((20,0), tree, fill="white")
                draw.bitmap((50,0), tree, fill="white")
                draw.bitmap((80,0), tree, fill="white")
          
        elif state == "OVERVIEW":
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
                 
        elif state == "RUN":
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

                  
                  
        elif state == "PAUSE":
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
                  
        elif state == "MODE_SELECT":
            
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
         
        elif state == "MODE_SETTINGS":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    draw.text((0,45), "P | Settings | "+ displayTime, font=fontSmall, fill="white")  # Removed cycles  # TODO do i add time to this while it's still playing?
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
                
        elif state == "MODE_SETTINGS_2":
            with canvas(device) as draw:
                draw.line((0, 45, 127 ,45), fill="white")
                if mode == "POMODORO_W" or mode == "POMODORO_B":
                    draw.text((0,45), "P | Settings | "+displayTime, font=fontSmall, fill="white")  # Removed cycles
                    draw.text((23, 0), "Set Break Time:", font=fontSmall, fill="white")
                    draw.text((17, 10), displayTime, font=fontBig, fill="white") #TODO Timing conversion printing
            
# ============================ MAIN ============================
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
t3 = Thread(target = runTree)
t3.start()

# ============================ FLASK ============================

app = Flask(__name__, static_folder='assets')
global taskDescr, empty
empty = "No Description"
taskDescr = [empty] * taskNum

@app.route("/")
def home():
    return redirect("/templates/index")

@app.route("/templates/index")
def home_template():
    global mode
    return render_template("index.html", displayCurrentMode=mode)


@app.route("/templates/task", methods=['POST', 'GET'])
def task_template():
    global mode
    global state
    global taskNum
    global taskDone
    global taskDescr
    global quantityON
    if not mode == "TASK":
        print("Changing mode to TASK and state RUN")
        mode = "TASK"
        state = "RUN"
        clearAll()
        quantityON = getAvailable() // taskNum
    if (taskDone == taskNum):
        taskDone = 0
        taskDescr = [empty] * taskNum 
        state = "WELCOME"
        return redirect("/templates/index")
        
        
    if request.method == "POST":

        if empty in taskDescr:
            result = taskDescr.index(empty)
            newDescr = request.form['taskDescr']
            whitespace = [not char or char.isspace() for char in newDescr] # Checking if nothing input then append empty string message
            if False in whitespace:
                taskDescr[result] = newDescr
            else:
                taskDescr[result] = empty
            

        
        else:    
            newDescr = request.form['taskDescr']
            whitespace = [not char or char.isspace() for char in newDescr] # Checking if nothing input then append empty string message
            if False in whitespace:
                taskDescr.append(newDescr)
            else:
                taskDescr.append(empty)
            
            taskNum = taskNum + 1
        
        
    return render_template("task.html", taskList=taskDescr, taskDone=taskDone, taskNum=taskNum)

@app.route("/task/pop")
def task_pop():
    global taskDone
    global state
    global taskDescr
    
    if (taskDone >= taskNum):
        print("Changing state to welcome")
        state = "WELCOME"
    else:
        taskDone = taskDone + 1
        quantityON = getAvailable() // taskNum
        taskDescr.pop(0)
    remainingTasks = taskNum - taskDone
    
    if remainingTasks == 0:
        
        allOn()
    else:
        if taskDone >=1:
            print("Turning on", quantityON, "LEDS")
            toggleNextLed(True, quantityON)
    
   
    return redirect("/templates/task")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)



# ========================================================


t1.join()
t2.join()
t3.join()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
