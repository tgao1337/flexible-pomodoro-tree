# flexible-pomodoro-tree

## Team members

* Shahzeb Naseer (sn2572@nyu.edu)

* Nicholas Coluccio (nc2294@nyu.edu)

* Tommy Gao (tg1759@nyu.edu)

## Description

A tree shaped device for flexible studying habits. 

The device will have three modes, one for a classic Pomodoro study session, another to track how many task are done, and one to take breaks based on a break budget.

## Subsystems

### LED and Drivers
Parts:
- LEDs and Drivers
  - 74HC595 Shift Register [datasheet: https://brightspace.nyu.edu/d2l/le/lessons/57774/topics/6119651]

### Display
Parts:
- OLED Display
  - SSD1106 Driver [link: https://www.amazon.com/MakerFocus-128X64-1-3-Inch-SSD1106/dp/B08V97FYD2]
  - SH1106 library used from Waveshare (https://www.waveshare.com/wiki/1.3inch_OLED_HAT) for SSD1106 display
### User Control
Parts:
- Buttons

### Timer
Parts:
- Buzzer
  - PS1240 [datasheet https://www.jp.tdk.com/tefe02/ef532_ps.pdf]
