#!/usr/bin/python

from Stepper import Motor
import RPi.GPIO as GPIO
import sys


if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)

	pin1 = int(sys.argv[1])
	pin2 = int(sys.argv[2])
	pin3 = int(sys.argv[3])
	pin4 = int(sys.argv[4])
	direction = int(sys.argv[5])
	angle = int(sys.argv[6])

	m = Motor([pin1,pin2,pin3,pin4], 15)
	if direction == -1:
		m.move_acw(angle)

	GPIO.cleanup()

