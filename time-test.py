from pomodoro import *
display = OLED()
display.setup()
display.clear()

def convertTime(value):  # given a number of seconds, returns string in HH:MM:SS format
    hours = value // 3600
    minutes = (value % 3600) // 60
    seconds = value % 60
    time = str(hours).rjust(2,'0') + ':' + str(minutes).rjust(2,'0') + ':' + str(seconds).rjust(2,'0')
    return time

pomoTime = 10
x = 10+1
for i in range(x):
    display.clear()
    display.text("Work Time:", 25, 0, 12)
    display.text(convertTime(pomoTime), 10, 10,25)
    print(convertTime(pomoTime))
    pomoTime = pomoTime - 1
    #time.sleep(1)
