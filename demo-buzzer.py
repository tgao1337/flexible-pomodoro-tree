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
  mario = ( (C6, .255 ),     (C6, .214 ),  (rest, .121 ),     (C6, .119 ), 
            (E6, .119 ),  (rest, .121 ),     (B5, .239 ),  (rest, .241 ), 
            (B4, .239 ),  (rest, .241 ),     (C6, .239 ),  (rest, .121 ), 
            (G5, .239 ),  (rest, .121 ),     (E5, .239 ),  (rest, .121 ), 
            (A5, .239 ),     (B5, .239 ),    (932, .119 ),     (A5, .119 ), 
         (rest, .121 ),     (G5, .159 ),     (E6, .159 ),     (G6, .159 ), 
            (A6, .239 ),     (F6, .119 ),     (G6, .119 ),  (rest, .121 ), 
            (E6, .239 ),     (C6, .119 ),     (D6, .119 ),     (B5, .119 ), 
         (rest, .241 ),     (C6, .239 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),     (E5, .239 ),  (rest, .121 ),     (A5, .239 ), 
            (B5, .239 ),    (932, .119 ),     (A5, .119 ),  (rest, .121 ), 
            (G5, .159 ),     (E6, .159 ),     (G6, .159 ),     (A6, .239 ), 
            (F6, .119 ),     (G6, .119 ),  (rest, .121 ),     (E6, .239 ), 
            (C6, .119 ),     (D6, .119 ),     (B5, .119 ),  (rest, .241 ), 
            (C5, .119 ),  (rest, .121 ),     (G6, .119 ),    (1480, .119 ), 
            (F6, .119 ),    (1245, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),    (831, .119 ),     (A5, .119 ),     (C6, .119 ), 
         (rest, .121 ),     (A5, .119 ),     (C6, .119 ),     (D6, .119 ), 
            (C5, .119 ),  (rest, .121 ),     (G6, .119 ),    (1480, .119 ), 
            (F6, .119 ),    (1245, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),     (E6, .119 ),  (rest, .121 ),     (E6, .238 ), 
         (rest, .121 ),     (G5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (G6, .119 ),    (1480, .119 ),     (F6, .119 ), 
           (1245, .119 ),  (rest, .121 ),     (C6, .119 ),  (rest, .121 ), 
           (831, .119 ),     (A5, .119 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),     (C6, .119 ),     (D6, .119 ),  (rest, .241 ), 
           (831, .119 ),  (rest, .241 ),     (G5, .119 ),  (rest, .241 ), 
            (E5, .119 ),  (rest, .241 ),     (G5, .238 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (G6, .119 ),    (1480, .119 ),     (F6, .119 ),    (1245, .119 ), 
         (rest, .121 ),     (C6, .119 ),  (rest, .121 ),    (831, .119 ), 
            (A5, .119 ),     (C6, .119 ),  (rest, .121 ),     (A5, .119 ), 
            (C6, .119 ),     (D6, .119 ),     (C5, .119 ),  (rest, .121 ), 
            (G6, .119 ),    (1480, .119 ),     (F6, .119 ),    (1245, .119 ), 
         (rest, .121 ),     (C6, .119 ),  (rest, .121 ),     (E6, .119 ), 
         (rest, .121 ),     (E6, .238 ),  (rest, .121 ),     (G5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (G6, .119 ), 
           (1480, .119 ),     (F6, .119 ),    (1245, .119 ),  (rest, .121 ), 
            (C6, .119 ),  (rest, .121 ),    (831, .119 ),     (A5, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (A5, .119 ),     (C6, .119 ), 
            (D6, .119 ),  (rest, .241 ),    (831, .119 ),  (rest, .241 ), 
            (G5, .119 ),  (rest, .241 ),     (E5, .119 ),  (rest, .241 ), 
            (G5, .238 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (E5, .119 ),     (C6, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),     (D6, .119 ),  (rest, .121 ), 
            (E6, .119 ),     (C6, .119 ),  (rest, .121 ),     (A5, .119 ), 
            (G5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (E5, .119 ),     (C6, .119 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),     (D6, .119 ),     (E6, .119 ), 
            (G5, .119 ),  (rest, .241 ),     (C5, .119 ),  (rest, .241 ), 
            (C5, .119 ),  (rest, .121 ),     (E5, .119 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),  (rest, .121 ),     (C6, .119 ), 
            (D6, .119 ),  (rest, .121 ),     (E6, .119 ),     (C6, .119 ), 
         (rest, .121 ),     (A5, .119 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (C6, .238 ),  (rest, .121 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),     (E6, .119 ), 
         (rest, .121 ),     (B5, .239 ),  (rest, .241 ),     (B4, .239 ), 
         (rest, .241 ),     (C6, .239 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),     (E5, .239 ),  (rest, .121 ),     (A5, .239 ), 
            (B5, .239 ),    (932, .119 ),     (A5, .119 ),  (rest, .121 ), 
            (G5, .159 ),     (E6, .159 ),     (G6, .159 ),     (A6, .239 ), 
            (F6, .119 ),     (G6, .119 ),  (rest, .121 ),     (E6, .239 ), 
            (C6, .119 ),     (D6, .119 ),     (B5, .119 ),  (rest, .241 ), 
            (C6, .239 ),  (rest, .121 ),     (G5, .239 ),  (rest, .121 ), 
            (E5, .239 ),  (rest, .121 ),     (A5, .239 ),     (B5, .239 ), 
           (932, .119 ),     (A5, .119 ),  (rest, .121 ),     (G5, .159 ), 
            (E6, .159 ),     (G6, .159 ),     (A6, .239 ),     (F6, .119 ), 
            (G6, .119 ),  (rest, .121 ),     (E6, .239 ),     (C6, .119 ), 
            (D6, .119 ),     (B5, .119 ),  (rest, .241 ),     (E6, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (G5, .239 ),  (rest, .121 ), 
           (831, .239 ),     (A5, .119 ),     (F6, .119 ),  (rest, .121 ), 
            (F6, .119 ),     (A5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (G5, .159 ),     (F6, .255 ),     (F6, .222 ), 
            (B5, .159 ),     (F6, .159 ),     (E6, .119 ),     (C6, .119 ), 
         (rest, .121 ),     (A5, .119 ),     (G5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (E6, .119 ),     (C6, .119 ), 
         (rest, .121 ),     (G5, .239 ),  (rest, .121 ),    (831, .239 ), 
            (A5, .119 ),     (F6, .119 ),  (rest, .121 ),     (F6, .119 ), 
            (A5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (G5, .119 ),     (A5, .119 ),  (rest, .121 ),     (A5, .255 ), 
            (A5, . 23 ),     (G5, .159 ),     (F5, .159 ),     (E5, .119 ), 
            (G5, .119 ),  (rest, .121 ),     (G5, .119 ),     (C5, .239 ), 
         (rest, .241 ),     (E6, .119 ),     (C6, .119 ),  (rest, .121 ), 
            (G5, .239 ),  (rest, .121 ),    (831, .239 ),     (A5, .119 ), 
            (F6, .119 ),  (rest, .121 ),     (F6, .119 ),     (A5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (G5, .159 ), 
            (F6, .255 ),     (F6, .222 ),     (B5, .159 ),     (F6, .159 ), 
            (E6, .119 ),     (C6, .119 ),  (rest, .121 ),     (A5, .119 ), 
            (G5, .119 ),  (rest, .121 ),     (C5, .119 ),  (rest, .121 ), 
            (E6, .119 ),     (C6, .119 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),    (831, .239 ),     (A5, .119 ),     (F6, .119 ), 
         (rest, .121 ),     (F6, .119 ),     (A5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (G5, .119 ),     (A5, .119 ), 
         (rest, .121 ),     (A5, .255 ),     (A5, . 23 ),     (G5, .159 ), 
            (F5, .159 ),     (E5, .119 ),     (G5, .119 ),  (rest, .121 ), 
            (G5, .119 ),     (C5, .239 ),  (rest, .241 ),     (E5, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),  (rest, .121 ), 
            (C6, .119 ),     (D6, .119 ),  (rest, .121 ),     (E6, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (A5, .119 ),     (G5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (E5, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),  (rest, .121 ), 
            (C6, .119 ),     (D6, .119 ),     (E6, .119 ),     (G5, .119 ), 
         (rest, .241 ),     (C5, .119 ),  (rest, .241 ),     (C5, .119 ), 
         (rest, .121 ),     (E5, .119 ),     (C6, .119 ),  (rest, .121 ), 
            (C6, .119 ),  (rest, .121 ),     (C6, .119 ),     (D6, .119 ), 
         (rest, .121 ),     (E6, .119 ),     (C6, .119 ),  (rest, .121 ), 
            (A5, .119 ),     (G5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (C6, .238 ),  (rest, .121 ),     (C6, .119 ), 
         (rest, .121 ),     (C6, .119 ),     (E6, .119 ),  (rest, .121 ), 
            (B5, .239 ),  (rest, .241 ),     (B4, .239 ),  (rest, .241 ), 
            (E6, .119 ),     (C6, .119 ),  (rest, .121 ),     (G5, .239 ), 
         (rest, .121 ),    (831, .239 ),     (A5, .119 ),     (F6, .119 ), 
         (rest, .121 ),     (F6, .119 ),     (A5, .119 ),  (rest, .121 ), 
            (C5, .119 ),  (rest, .121 ),     (G5, .159 ),     (F6, .255 ), 
            (F6, .222 ),     (B5, .159 ),     (F6, .159 ),     (E6, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (A5, .119 ),     (G5, .119 ), 
         (rest, .121 ),     (C5, .119 ),  (rest, .121 ),     (E6, .119 ), 
            (C6, .119 ),  (rest, .121 ),     (G5, .239 ),  (rest, .121 ), 
           (831, .239 ),     (A5, .119 ),     (F6, .119 ),  (rest, .121 ), 
            (F6, .119 ),     (A5, .119 ),  (rest, .121 ),     (C5, .119 ), 
         (rest, .121 ),     (G5, .119 ),     (A5, .119 ),  (rest, .121 ), 
            (A5, .255 ),     (A5, . 23 ),     (G5, .159 ),     (F5, .159 ), 
            (E5, .119 ),     (G5, .119 ),  (rest, .121 ),     (G5, .119 ), 
            (C5, .239 ))
  playList(mario)

buzzerSetup()
playMario()
