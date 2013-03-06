#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys
import datetime

#import thread
import threading

class MotorThread(threading.Thread):
	def __init__(self, pin1, pin2, pin3, pin4, command_index):
		threading.Thread.__init__(self)
		self.pin1 = int(pin1)
		self.pin2 = int(pin2)
		self.pin3 = int(pin3)
		self.pin4 = int(pin4)
		self.command_index = int(command_index)

		self.motor = Motor([int(self.pin1), int(self.pin2), int(self.pin3), int(self.pin4)], 15)

	def run(self):
		self.motor.move_to(90)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	try:
		mFL = MotorThread( 8, 10, 12, 16, 1)
		mFR = MotorThread(18, 22, 24, 26, 2)
		mBL = MotorThread( 3,  5,  7, 11, 3)
		mBR = MotorThread(15, 19, 21, 23, 4)

		mFL.start()
		mFR.start()
		mBL.start()
		#mBR.start()


	except Exception as inst:
		print("Error: unable to start thread")
		print(type(inst))
		print(inst.args)
		print(inst)

	while True:
		pass

	GPIO.cleanup()

