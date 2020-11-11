#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RELAIS_1_GPIO = 4
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

time.sleep(0.5)

GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out

GPIO.cleanup()

print "open"
