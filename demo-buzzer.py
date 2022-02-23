from buzzer import *

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
  mario = ( (E6, .000 ),     (C6, .111 ),  (rest, .001 ),     (E6, .000 ), 
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
            (B5, .239 ),  (rest, .241 ),     (G5, .000 ),     (B4, .239 ), 
         (rest, .241 ),     (C6, .239 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),     (E5, .239 ),  (rest, .121 ),     (A5, .239 ), 
         (rest, .001 ),     (B5, .239 ),  (rest, .001 ),    (932, .119 ), 
         (rest, .001 ),     (A5, .119 ),  (rest, .121 ),     (G5, .159 ), 
         (rest, .001 ),     (E6, .159 ),  (rest, .001 ),     (G6, .159 ), 
         (rest, .001 ),     (A6, .239 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .001 ),     (G6, .119 ),  (rest, .121 ),     (E6, .239 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .001 ),     (D6, .119 ), 
         (rest, .001 ),     (B5, .119 ),  (rest, .241 ),     (C6, .239 ), 
         (rest, .121 ),     (G5, .239 ),  (rest, .121 ),     (E5, .239 ), 
         (rest, .121 ),     (A5, .239 ),  (rest, .001 ),     (B5, .239 ), 
         (rest, .001 ),    (932, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .121 ),     (G5, .159 ),  (rest, .001 ),     (E6, .159 ), 
         (rest, .001 ),     (G6, .159 ),  (rest, .001 ),     (A6, .239 ), 
         (rest, .001 ),     (F6, .119 ),  (rest, .001 ),     (G6, .119 ), 
         (rest, .121 ),     (E6, .239 ),  (rest, .001 ),     (C6, .119 ), 
         (rest, .001 ),     (D6, .119 ),  (rest, .001 ),     (B5, .119 ), 
         (rest, .241 ),     (E6, .119 ),  (rest, .001 ),     (C6, .119 ), 
         (rest, .121 ),     (G5, .239 ),  (rest, .121 ),    (831, .239 ), 
         (rest, .001 ),     (A5, .119 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .121 ),     (F6, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (B5, .000 ), 
            (G5, .159 ),  (rest, .001 ),     (A6, .000 ),     (F6, .159 ), 
         (rest, .001 ),     (A6, .000 ),     (F6, .159 ),  (rest, .001 ), 
            (A6, .000 ),     (F6, .159 ),  (rest, .001 ),     (G6, .000 ), 
            (B5, .159 ),  (rest, .001 ),     (F6, .159 ),  (rest, .001 ), 
            (E6, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),  (rest, .001 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (E6, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (G5, .239 ),  (rest, .121 ), 
           (831, .239 ),  (rest, .001 ),     (A5, .119 ),  (rest, .001 ), 
            (F6, .119 ),  (rest, .121 ),     (F6, .119 ),  (rest, .001 ), 
            (A5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (B5, .000 ),     (G5, .119 ),  (rest, .001 ),     (F6, .000 ), 
            (A5, .119 ),  (rest, .121 ),     (F6, .000 ),     (A5, .119 ), 
         (rest, .001 ),     (F6, .000 ),     (A5, .159 ),  (rest, .001 ), 
            (E6, .000 ),     (G5, .159 ),  (rest, .001 ),     (D6, .000 ), 
            (F5, .159 ),  (rest, .001 ),     (C6, .000 ),     (E5, .119 ), 
         (rest, .001 ),     (G5, .119 ),  (rest, .121 ),     (G5, .119 ), 
         (rest, .001 ),     (C5, .239 ),  (rest, .241 ),     (E6, .119 ), 
         (rest, .001 ),     (C6, .119 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),    (831, .239 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .001 ),     (F6, .119 ),  (rest, .121 ),     (F6, .119 ), 
         (rest, .001 ),     (A5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (B5, .000 ),     (G5, .159 ),  (rest, .001 ), 
            (A6, .000 ),     (F6, .159 ),  (rest, .001 ),     (A6, .000 ), 
            (F6, .159 ),  (rest, .001 ),     (A6, .000 ),     (F6, .159 ), 
         (rest, .001 ),     (G6, .000 ),     (B5, .159 ),  (rest, .001 ), 
            (F6, .159 ),  (rest, .001 ),     (E6, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (A5, .119 ),  (rest, .001 ), 
            (G5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (E6, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (G5, .239 ),  (rest, .121 ),    (831, .239 ),  (rest, .001 ), 
            (A5, .119 ),  (rest, .001 ),     (F6, .119 ),  (rest, .121 ), 
            (F6, .119 ),  (rest, .001 ),     (A5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (B5, .000 ),     (G5, .119 ), 
         (rest, .001 ),     (F6, .000 ),     (A5, .119 ),  (rest, .121 ), 
            (F6, .000 ),     (A5, .119 ),  (rest, .001 ),     (F6, .000 ), 
            (A5, .159 ),  (rest, .001 ),     (E6, .000 ),     (G5, .159 ), 
         (rest, .001 ),     (D6, .000 ),     (F5, .159 ),  (rest, .001 ), 
            (C6, .000 ),     (E5, .119 ),  (rest, .001 ),     (G5, .119 ), 
         (rest, .121 ),     (G5, .119 ),  (rest, .001 ),     (C5, .239 ), 
         (rest, .241 ),     (C6, .000 ),     (E5, .119 ),  (rest, .001 ), 
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
            (B5, .239 ),  (rest, .241 ),     (G5, .000 ),     (B4, .239 ), 
         (rest, .241 ),     (E6, .119 ),  (rest, .001 ),     (C6, .119 ), 
         (rest, .121 ),     (G5, .239 ),  (rest, .121 ),    (831, .239 ), 
         (rest, .001 ),     (A5, .119 ),  (rest, .001 ),     (F6, .119 ), 
         (rest, .121 ),     (F6, .119 ),  (rest, .001 ),     (A5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (B5, .000 ), 
            (G5, .159 ),  (rest, .001 ),     (A6, .000 ),     (F6, .159 ), 
         (rest, .001 ),     (A6, .000 ),     (F6, .159 ),  (rest, .001 ), 
            (A6, .000 ),     (F6, .159 ),  (rest, .001 ),     (G6, .000 ), 
            (B5, .159 ),  (rest, .001 ),     (F6, .159 ),  (rest, .001 ), 
            (E6, .119 ),  (rest, .001 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),  (rest, .001 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (E6, .119 ),  (rest, .001 ), 
            (C6, .119 ),  (rest, .121 ),     (G5, .239 ),  (rest, .121 ), 
           (831, .239 ),  (rest, .001 ),     (A5, .119 ),  (rest, .001 ), 
            (F6, .119 ),  (rest, .121 ),     (F6, .119 ),  (rest, .001 ), 
            (A5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (B5, .000 ),     (G5, .119 ),  (rest, .001 ),     (F6, .000 ), 
            (A5, .119 ),  (rest, .121 ),     (F6, .000 ),     (A5, .119 ), 
         (rest, .001 ),     (F6, .000 ),     (A5, .159 ),  (rest, .001 ), 
            (E6, .000 ),     (G5, .159 ),  (rest, .001 ),     (D6, .000 ), 
            (F5, .159 ),  (rest, .001 ),     (C6, .000 ),     (E5, .119 ), 
         (rest, .001 ),     (G5, .119 ),  (rest, .121 ),     (G5, .119 ), 
         (rest, .001 ),     (C5, .239 ))
  playList(mario)

buzzerSetup()
playMario()
