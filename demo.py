# this is the start for pomodoro demo

from pomodoro import *

def buzz():
    # Set frequency as a variable
    C7 = 2093
    # creating a list of tuples containing frequencies and duration
    scale = [(1319, 1), (1397, 1), (1568, 1), (1760, 1), (1976, 1), (C7, 1)]
    # Run setup code to start hardware PWM
    buzzerSetup()
    # Play 4000 Hz for 1 second
    playTime(1)
    # Then using different methods, play a scale
    playFreq(1047) # Frequency for C6
    time.sleep(1) # Wait one second
    playStop() # Stop playing after one second
    playFreqTime(1175, 1) # Play D6 for one second
    playList(scale) # play E6, F6, G6, A6, B6, and C7 for one second each.


def test_display():
    display = OLED()
    display.text("Pomodoro Tree", 10, 0, 15)
    display.draw_line(0,20,127,20)

if __name__ == "__main__":
    test_display()
