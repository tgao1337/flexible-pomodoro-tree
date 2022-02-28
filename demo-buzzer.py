from buzzer import *

def playScale():
  # Set frequency as a variable
  C7 = 2093

  # creating a list of tuples containing frequencies and duration
  Scale = [(1382, 1), (1397, 1), (1568, 1), (1760, 1), (1976, 1), (C7, 1)]

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
  # Variables can also be used as seen for C7. A list of variables can be found in the next section.

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
  
def playMario():
  # this song was found on midi here: https://bitmidi.com/mario-bros-super-mario-bros-theme-mid
  # this converter helped with the timings: https://sparks.gogo.co.nz/midi_tone.html
  mario = [ (E6, .000 ),     (C6, .111 ),  (rest, .001 ),     (E6, .000 ), 
            (C6, .239 ),  (rest, .001 ),     (E6, .000 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),  (rest, .001 ),     (E6, .119 ), 
         (rest, .121 ),     (G6, .000 ),     (B5, .239 ),  (rest, .241 ), 
            (G5, .000 ),     (B4, .239 ),  (rest, .241 ),     (C6, .239 ), 
         (rest, .121 ),     (G5, .239 ),  (rest, .121 ),     (E5, .239 ), 
         (rest, .121 ),     (A5, .239 ),  (rest, .001 ),     (B5, .239 ), 
         (rest, .001 ),    (932, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .121 ),     (G5, .159 ),  (rest, .001 ),     (E6, .159 ), 
         (rest, .001 ),     (G6, .159 ),  (rest, .001 ),     (A6, .239 ), 
         (rest, .001 ),     (F6, .119 ),  (rest, .001 ),     (G6, .119 ), 
         (rest, .121 ),     (E6, .239 ),  (rest, .001 ),     (C6, .119 ), 
         (rest, .001 ),     (D6, .119 ),  (rest, .001 ),     (B5, .119 ), 
         (rest, .241 ),     (C6, .239 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),     (E5, .239 ),  (rest, .121 ),     (A5, .239 ), 
         (rest, .001 ),     (B5, .239 ),  (rest, .001 ),    (932, .119 ), 
         (rest, .001 ),     (A5, .119 ),  (rest, .121 ),     (G5, .159 ), 
         (rest, .001 ),     (E6, .159 ),  (rest, .001 ),     (G6, .159 ), 
         (rest, .001 ),     (A6, .239 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .001 ),     (G6, .119 ),  (rest, .121 ),     (E6, .239 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .001 ),     (D6, .119 ), 
         (rest, .001 ),     (B5, .119 ),  (rest, .241 ),     (C5, .119 ), 
         (rest, .121 ),     (G6, .119 ),  (rest, .001 ),    (1480, .119 ), 
         (rest, .001 ),     (F6, .119 ),  (rest, .001 ),    (1245, .119 ), 
         (rest, .121 ),     (E6, .000 ),     (C6, .119 ),  (rest, .121 ), 
           (831, .119 ),  (rest, .001 ),     (A5, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (A5, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .001 ),     (D6, .119 ),  (rest, .001 ), 
            (C5, .119 ),  (rest, .121 ),     (G6, .119 ),  (rest, .001 ), 
           (1480, .119 ),  (rest, .001 ),     (F6, .119 ),  (rest, .001 ), 
           (1245, .119 ),  (rest, .121 ),     (E6, .000 ),     (C6, .119 ), 
         (rest, .121 ),     (C7, .000 ),     (E6, .119 ),  (rest, .121 ), 
            (C7, .000 ),     (E6, .119 ),  (rest, .001 ),     (C7, .000 ), 
            (E6, .119 ),  (rest, .121 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (G6, .119 ),  (rest, .001 ), 
           (1480, .119 ),  (rest, .001 ),     (F6, .119 ),  (rest, .001 ), 
           (1245, .119 ),  (rest, .121 ),     (E6, .000 ),     (C6, .119 ), 
         (rest, .121 ),    (831, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .121 ),     (A5, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .001 ),     (D6, .119 ), 
         (rest, .241 ),    (1245, .000 ),    (831, .119 ),  (rest, .241 ), 
            (D6, .000 ),     (G5, .119 ),  (rest, .241 ),     (C6, .000 ), 
            (E5, .119 ),  (rest, .241 ),     (G5, .119 ),  (rest, .001 ), 
            (G5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (G6, .119 ),  (rest, .001 ), 
           (1480, .119 ),  (rest, .001 ),     (F6, .119 ),  (rest, .001 ), 
           (1245, .119 ),  (rest, .121 ),     (E6, .000 ),     (C6, .119 ), 
         (rest, .121 ),    (831, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .121 ),     (A5, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .001 ),     (D6, .119 ), 
         (rest, .001 ),     (C5, .119 ),  (rest, .121 ),     (G6, .119 ), 
         (rest, .001 ),    (1480, .119 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .001 ),    (1245, .119 ),  (rest, .121 ),     (E6, .000 ), 
            (C6, .119 ),  (rest, .121 ),     (C7, .000 ),     (E6, .119 ), 
         (rest, .121 ),     (C7, .000 ),     (E6, .119 ),  (rest, .001 ), 
            (C7, .000 ),     (E6, .119 ),  (rest, .121 ),     (G5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (G6, .119 ), 
         (rest, .001 ),    (1480, .119 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .001 ),    (1245, .119 ),  (rest, .121 ),     (E6, .000 ), 
            (C6, .119 ),  (rest, .121 ),    (831, .119 ),  (rest, .001 ), 
            (A5, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .001 ), 
            (D6, .119 ),  (rest, .241 ),    (1245, .000 ),    (831, .119 ), 
         (rest, .241 ),     (D6, .000 ),     (G5, .119 ),  (rest, .241 ), 
            (C6, .000 ),     (E5, .119 ),  (rest, .241 ),     (G5, .119 ), 
         (rest, .001 ),     (G5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (C6, .000 ),     (E5, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),  (rest, .121 ), 
            (C6, .119 ),  (rest, .001 ),     (D6, .119 ),  (rest, .121 ), 
            (E6, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),  (rest, .001 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (C6, .000 ),     (E5, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),  (rest, .001 ),     (D6, .119 ), 
         (rest, .001 ),     (E6, .119 ),  (rest, .001 ),     (G5, .119 ), 
         (rest, .241 ),     (C5, .119 ),  (rest, .241 ),     (C5, .119 ), 
         (rest, .121 ),     (C6, .000 ),     (E5, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),  (rest, .121 ), 
            (C6, .119 ),  (rest, .001 ),     (D6, .119 ),  (rest, .121 ), 
            (E6, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),  (rest, .001 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (E6, .000 ),     (C6, .119 ), 
         (rest, .001 ),     (E6, .000 ),     (C6, .119 ),  (rest, .121 ), 
            (E6, .000 ),     (C6, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .001 ),     (E6, .119 ),  (rest, .121 ),     (G6, .000 ), 
            (B5, .239 ),  (rest, .241 ),     (G5, .000 )]

  playList(mario)
  
def playJingle():
  jingle = ((G5, .255 ),     (G5, .001 ),  (rest, .000 ),     (G5, .255 ), 
            (G5, .001 ),     (E6, .255 ),     (E6, .001 ),  (rest, .000 ), 
            (D6, .255 ),     (D6, .001 ),  (rest, .000 ),     (C6, .255 ), 
            (C6, .001 ),  (rest, .000 ),     (G5, .255 ),     (G5, .255 ), 
            (G5, .255 ),     (G5, .003 ),  (rest, .000 ),     (G5, .255 ), 
            (G5, .001 ),  (rest, .000 ),     (G5, .255 ),     (G5, .001 ), 
            (E6, .255 ),     (E6, .001 ),  (rest, .000 ),     (D6, .255 ), 
            (D6, .001 ),  (rest, .000 ),     (C6, .255 ),     (C6, .001 ), 
         (rest, .000 ),     (A5, .255 ),     (A5, .255 ),     (A5, .255 ), 
            (A5, .003 ),  (rest, .000 ),     (A5, .255 ),     (A5, .001 ), 
         (rest, .000 ),     (A5, .255 ),     (A5, .001 ),     (F6, .255 ), 
            (F6, .001 ),  (rest, .000 ),     (E6, .255 ),     (E6, .001 ), 
         (rest, .000 ),     (D6, .255 ),     (D6, .001 ),  (rest, .000 ), 
            (B5, .255 ),     (B5, .255 ),     (B5, .255 ),     (B5, .255 ), 
            (B5, .004 ),  (rest, .000 ),     (G6, .000 ),     (B5, .255 ), 
            (B5, .001 ),  (rest, .000 ),     (G6, .255 ),     (G6, .001 ), 
         (rest, .000 ),     (F6, .255 ),     (F6, .001 ),  (rest, .000 ), 
            (D6, .255 ),     (D6, .001 ),  (rest, .000 ),     (E6, .000 ), 
            (C6, .255 ),     (C6, .255 ),     (C6, .255 ),     (C6, .003 ), 
         (rest, .000 ),     (G5, .255 ),     (G5, .001 ),  (rest, .000 ), 
            (G5, .255 ),     (G5, .001 ),     (E6, .255 ),     (E6, .001 ), 
         (rest, .000 ),     (D6, .255 ),     (D6, .001 ),  (rest, .000 ), 
            (C6, .255 ),     (C6, .001 ),  (rest, .000 ),     (G5, .255 ), 
            (G5, .255 ),     (G5, .255 ),     (G5, .003 ),  (rest, .000 ), 
            (G5, .255 ),     (G5, .001 ),  (rest, .000 ),     (G5, .255 ), 
            (G5, .001 ),     (E6, .255 ),     (E6, .001 ),  (rest, .000 ), 
            (D6, .255 ),     (D6, .001 ),  (rest, .000 ),     (C6, .255 ), 
            (C6, .001 ),  (rest, .000 ),     (A5, .255 ),     (A5, .255 ), 
            (A5, .255 ),     (A5, .003 ),  (rest, .000 ),     (A5, .255 ), 
            (A5, .001 ),  (rest, .000 ),     (A5, .255 ),     (A5, .001 ), 
            (F6, .255 ),     (F6, .001 ),  (rest, .000 ),     (E6, .255 ), 
            (E6, .001 ),  (rest, .000 ),     (D6, .255 ),     (D6, .001 ), 
         (rest, .000 ),     (G6, .000 ),     (B5, .255 ),     (B5, .001 ), 
         (rest, .000 ),     (G6, .255 ),     (G6, .001 ),  (rest, .000 ), 
            (G6, .255 ),     (G6, .001 ),  (rest, .000 ),     (G6, .255 ), 
            (G6, .001 ),  (rest, .000 ),     (A6, .000 ),     (B5, .255 ), 
            (B5, .001 ),  (rest, .000 ),     (G6, .255 ),     (G6, .001 ), 
         (rest, .000 ),     (F6, .255 ),     (F6, .001 ),  (rest, .000 ), 
            (D6, .255 ),     (D6, .001 ),  (rest, .000 ),     (C6, .255 ), 
            (C6, .255 ),     (C6, .002 ),  (rest, .000 ),     (G6, .255 ), 
            (G6, .255 ),     (G6, .002 ),  (rest, .000 ),     (E6, .000 ), 
            (C6, .255 ),     (C6, .001 ),  (rest, .000 ),     (E6, .255 ), 
            (E6, .001 ),  (rest, .000 ),     (E6, .000 ),     (G5, .255 ), 
            (G5, .255 ),     (G5, .002 ),  (rest, .000 ),     (E6, .000 ), 
            (C6, .255 ),     (C6, .001 ),  (rest, .000 ),     (E6, .255 ), 
            (E6, .001 ),  (rest, .000 ),     (E6, .000 ),     (G5, .255 ), 
            (G5, .255 ),     (G5, .002 ),  (rest, .000 ),     (E6, .000 ), 
            (C6, .255 ),     (C6, .001 ),  (rest, .000 ),     (G6, .255 ), 
            (G6, .001 ),  (rest, .000 ),     (C6, .000 ),     (G5, .255 ), 
            (G5, .001 ),  (rest, .000 ),     (D6, .255 ),     (D6, .001 ), 
         (rest, .000 ),     (C6, .000 ),     (E6, .255 ),     (E6, .255 ), 
            (E6, .002 ),  (rest, .000 ),     (G5, .255 ),     (G5, .255 ), 
            (G5, .002 ),  (rest, .000 ),     (F6, .000 ),     (B5, .255 ), 
            (B5, .001 ),  (rest, .000 ),     (F6, .255 ),     (F6, .001 ), 
         (rest, .000 ),     (F6, .000 ),     (G5, .255 ),     (G5, .001 ), 
         (rest, .000 ),     (F6, .255 ),     (F6, .001 ),  (rest, .000 ), 
            (F6, .000 ),     (C6, .255 ),     (C6, .001 ),     (E6, .005 ), 
         (rest, .251 ),     (E6, .000 ),     (G5, .255 ),     (G5, .001 ), 
         (rest, .000 ),     (E6, .255 ),     (E6, .001 ),  (rest, .000 ), 
            (E6, .000 ),    (740, .255 ),    (740, .001 ),     (D6, .005 ), 
         (rest, .251 ),     (D6, .255 ),     (D6, .001 ),  (rest, .000 ), 
            (E6, .255 ),     (E6, .001 ),  (rest, .000 ),     (D6, .000 ), 
            (G5, .255 ),     (G5, .255 ),     (G5, .002 ),  (rest, .000 ), 
            (G6, .255 ),     (G6, .255 ),     (G6, .002 ),  (rest, .000 ), 
            (E6, .000 ),     (C6, .255 ),     (C6, .001 ),  (rest, .000 ), 
            (E6, .255 ),     (E6, .001 ),  (rest, .000 ),     (E6, .000 ), 
            (G5, .255 ),     (G5, .255 ),     (G5, .002 ),  (rest, .000 ), 
            (E6, .000 ),     (C6, .255 ),     (C6, .001 ),  (rest, .000 ), 
            (E6, .255 ),     (E6, .001 ),  (rest, .000 ),     (E6, .000 ), 
            (G5, .255 ),     (G5, .255 ),     (G5, .002 ),  (rest, .000 ), 
            (E6, .000 ),     (C6, .255 ),     (C6, .001 ),  (rest, .000 ), 
            (G6, .255 ),     (G6, .001 ),  (rest, .000 ),     (C6, .000 ), 
            (G5, .255 ),     (G5, .001 ),  (rest, .000 ),     (D6, .255 ), 
            (D6, .001 ),  (rest, .000 ),     (C6, .000 ),     (E6, .255 ), 
            (E6, .255 ),     (E6, .002 ),  (rest, .000 ),     (G5, .255 ), 
            (G5, .255 ),     (G5, .002 ),  (rest, .000 ),     (F6, .000 ), 
            (B5, .255 ),     (B5, .001 ),  (rest, .000 ),     (F6, .255 ), 
            (F6, .001 ),  (rest, .000 ),     (F6, .000 ),     (G5, .255 ), 
            (G5, .001 ),  (rest, .000 ),     (F6, .255 ),     (F6, .001 ), 
         (rest, .000 ),     (F6, .000 ),     (C6, .255 ),     (C6, .001 ), 
            (E6, .005 ),  (rest, .251 ),     (E6, .000 ),     (G5, .255 ), 
            (G5, .001 ),  (rest, .000 ),     (E6, .255 ),     (E6, .001 ), 
         (rest, .000 ),     (G6, .000 ),     (G5, .255 ),     (G5, .001 ), 
         (rest, .000 ),     (G6, .000 ),     (G5, .255 ),     (G5, .001 ), 
         (rest, .000 ),     (A5, .000 ),     (F6, .255 ),     (F6, .001 ), 
         (rest, .000 ),     (D6, .000 ),     (B5, .005 ),  (rest, .251 ), 
            (C6, .255 ),     (C6, .255 ),     (C6, .255 ),     (C6, .003 ), 
         (rest, .000 ))
  playList(jingle)

# buzzerSetup()
# playMario()

# playJingle() # sounds bad :(

playScale() # This has the buzzerSetup already
