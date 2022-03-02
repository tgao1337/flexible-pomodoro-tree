# This is the Flexible Pomodoro Tree official code
from pomodoro import *

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
