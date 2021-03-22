#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# header pin numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)

while 1:
	GPIO.output(25, GPIO.LOW)
        time.sleep(1)
#	GPIO.output(18, GPIO.LOW)
#        time.sleep(1)
	break	
