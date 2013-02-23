#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	m = Motor([18,22,24,26], 10)
	#print "Pause in seconds: " + `m._T`

	# anti-clock 90
	print "Anti clock 90 degrees"
	m.move_to(90)
	sleep(1)

	# clockw 90
	print "Clockwise 90 degrees"
	m.move_to(0)
	sleep(1)

	# anti-clock 180
	print "Anti-clock 180"
	m.move_to(180)
	sleep(1)

	# clock 180
	print "Clock 180"
	m.move_to(90)
	m.move_to(0)
	sleep(1)
	GPIO.cleanup()

