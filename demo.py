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

def test_leds():
   setup()

  allOn()
  time.sleep(0.05)  
  clearAll()
  #turn on one by one, and then off
  for i in range(29):
   toggleNextLed(True)

  for i in range(29):
   toggleNextLed(False)

#turn on by color group then off
  toggleClusterColorGroup(1,'r',True)
  toggleClusterColorGroup(2,'r',True)
  toggleClusterColorGroup(3,'r',True)
  toggleClusterColorGroup(4,'r',True)

  toggleClusterColorGroup(1,'y',True)
  toggleClusterColorGroup(2,'y',True)
  toggleClusterColorGroup(3,'y',True)
  toggleClusterColorGroup(4,'y',True)

  toggleClusterColorGroup(1,'g',True)
  toggleClusterColorGroup(2,'g',True)
  toggleClusterColorGroup(3,'g',True)
  toggleClusterColorGroup(4,'g',True)

  toggleClusterColorGroup(1,'g',False)
  toggleClusterColorGroup(2,'g',False)
  toggleClusterColorGroup(3,'g',False)
  toggleClusterColorGroup(4,'g',False)

  toggleClusterColorGroup(1,'y',False)
  toggleClusterColorGroup(2,'y',False)
  toggleClusterColorGroup(3,'y',False)
  toggleClusterColorGroup(4,'y',False)

  toggleClusterColorGroup(1,'r',False)
  toggleClusterColorGroup(2,'r',False)
  toggleClusterColorGroup(3,'r',False)
  toggleClusterColorGroup(4,'r',False)

#mix up order of on off to ensure that toggleLed always finds corrrect next LED.
  toggleClusterColorGroup(2,'y',True)
  toggleNextLed(False)
  toggleNextLed(True)
  toggleNextLed(True)
  toggleNextLed(False)
  toggleClusterColorGroup(1,'y',True)
  toggleNextLed(False)
  toggleClusterColorGroup(3,'r',True)
  toggleNextLed(False)
  toggleClusterColorGroup(2,'g',True)
  allOn()
  selectClusterOFF(2)
  selectClusterOFF(4)
  selectClusterOFF(3)
  toggleNextLed(True)
  selectClusterOFF(1)



if __name__ == "__main__":
    test_display()
    test_leds()
    buzz()
