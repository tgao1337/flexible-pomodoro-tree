from buzzer import *

# variables used to translate notes to frequencies
rest = 0
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523
D5 = 587
E5 = 659
F5 = 698
G5 = 784
A5 = 880
B5 = 988
C6 = 1047
D6 = 1175
E6 = 1382
F6 = 1397
G6 = 1568
A6 = 1760
B6 = 1976
C7 = 2093
D7 = 2349
E7 = 2637
F7 = 2794
G7 = 3136
A7 = 3520
B7 = 3951
C8 = 4186

def playHCB():
  playFreq(3951)
  playFreq(3520)
  playFreq(3136)

  playFreqTime(0, .5)
  playFreq(3951)
  playFreq(3520)
  playFreq(3136)

  playFreqTime(0, .5)
  playFreqTime(3136, .25)
  playFreqTime(0, .25)
  playFreqTime(3136, .25)
  playFreqTime(0, .25)
  playFreqTime(3136, .25)
  playFreqTime(0, .25)
  playFreqTime(3136, .25)
  playFreqTime(0, .5)
  playFreqTime(3520, .25)
  playFreqTime(0, .25)
  playFreqTime(3520, .25)
  playFreqTime(0, .25)
  playFreqTime(3520, .25)
  playFreqTime(0, .25)
  playFreqTime(3520, .25)
  playFreqTime(0, .5)

  playFreq(3951)
  playFreq(3520)
  playFreq(3136)

playList(((B6, .4), (A6, .4), (G6, .4)))
