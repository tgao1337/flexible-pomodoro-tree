from pomodoro import *

display = OLED()
display.setup()

display.clear()
#display.draw_line(0, 45, 127 ,45)
#display.text("Select Mode", 30,45,12)
display.text("Select Mode:\n > Pomodoro \n    Task \n    Budget", 20,0,12)
display.clear()
display.text("Select Mode:\n    Pomodoro \n > Task \n    Budget", 20,0,12)
display.clear()
display.text("Select Mode:\n    Pomodoro \n    Task \n > Budget", 20,0,12)
#display.text(" Pomodoro \n Task \n > Budget", 0,0,12)

'''
display.clear()
display.draw_line(0, 45, 127 ,45)
display.text("Select Mode", 30,45,12)
display.text("Pomodoro", 32,0,14)
display.text("> Task", 20,12,14)
display.text("Budget", 32,24,14)
'''
display.clear()
display.draw_line(0, 45, 127 ,45)
display.text("Select Mode", 30,45,12)
display.text("Pomodoro", 32,0,14)
display.text("Task", 32,12,14)
display.text("> Budget", 20,24,14)

display.clear()

display.text("WELCOME" , 0, 0, 25)
