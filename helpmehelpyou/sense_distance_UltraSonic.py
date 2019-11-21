import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import csv
import os
import subprocess
from time import sleep
import random

TRIG = 23   #When we say TRIG, we mean 23. Makes the code easier to understand.
ECHO = 24   #When we say ECHO, we mean 24. Makes the code easier to understand.

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)    #sets up TRIG (that's PIN 23) to an outout for the speaker to trigger sending a PING!
GPIO.setup(ECHO,GPIO.IN)     #sets up ECHO (that's PIN 23) to an input microphone to listen for the echo PONG back.

GPIO.output(TRIG, False)     #Makes sure the Trigger speaker isn't sending out anything and is quiet to start.
print ("Waiting For Sensor To Settle")
time.sleep(2)


def distcheck():  #defines a neat function to gather up all the code needed for one single distance measurement.

  GPIO.output(TRIG, True)  #fires a pulse by setting the trigger speaker to high
  time.sleep(0.00001)      #wait's a fraction of a second, it's a very short pulse!!!!
  GPIO.output(TRIG, False) #turns the trigger speaker off again.

  while GPIO.input(ECHO)==0:    #measure some times
    pulse_start = time.time()   #records the time the pulse was sent

  while GPIO.input(ECHO)==1:    #records the time the echo was heard
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start  #finds the differnce between sent and recieved pulses

  distance = pulse_duration * 17150         #multiply by a fudge factor to convert to seconds

  distance = round(distance, 2)             #rounds off the number

  #print ("Distance:",distance,"cm")         #prints it
  return distance


######## Start of program #########
while True:
    print(distcheck())                                #runs the function above


    if distcheck() <= 40 :
        introNumber = random.randint(1, 9)

        if introNumber==1:
            sleep(2)
            os.system('mplayer morgan.m4a&')
            sleep(3)
            
        elif introNumber==2:
            sleep(2)
            os.system('mplayer raheem.m4a&')
            sleep(3)
            
        elif introNumber==3:
            sleep(2)
            os.system('mplayer sadbh.m4a&')
            sleep(3)
            
        elif introNumber==4:
            sleep(2)
            os.system('mplayer danielob.m4a&')
            sleep(3)
            
        elif introNumber==5:
            sleep(2)
            os.system('mplayer raheem2.m4a&')
            sleep(3)
            
        elif introNumber==6:
            os.system('mplayer todd.m4a&')
            sleep(4)
            
        elif introNumber==7:
            os.system('mplayer mrohara.m4a&')
            sleep(4)
            
        elif introNumber==8:
            os.system('mplayer mrworrel.m4a&')
            sleep(4)

        elif introNumber==9:
            os.system('mplayer mshayden.m4a&')
            sleep(4)
        
                
        
        
        
        
    #else distcheck == >40:


GPIO.cleanup()                              #clears any GPIO pins that might have been left set to on.


