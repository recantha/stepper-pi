#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	m = Motor([int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])], 15)

	# clock 180
	m.move_to(180)
	sleep(0.2)
	m.move_to(270)
	sleep(0.5)
	m.move_to(0)
	m.move_to(-90)
	GPIO.cleanup()

