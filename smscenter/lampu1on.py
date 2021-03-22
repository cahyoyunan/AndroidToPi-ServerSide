#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# header pin numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

while 1:
	GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
#	GPIO.output(18, GPIO.LOW)
#        time.sleep(1)
	break	
