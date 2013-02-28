#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	m = Motor([18,22,24,26], 10)
	#print "Pause in seconds: " + `m._T`

	# clock 180
	print "Clock 180"
	m.move_to(90)
	sleep(0.5)
	m.move_to(0)
	sleep(0.5)
	GPIO.cleanup()

