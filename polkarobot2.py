#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys
import datetime

#import thread
#import threading
import multiprocessing

#		self.motor.move_to(90)

def createMotor(pin1, pin2, pin3, pin4, command_index):
	pin1 = int(pin1)
	pin2 = int(pin2)
	pin3 = int(pin3)
	pin4 = int(pin4)
	command_index = int(command_index)

	motor = Motor([pin1,pin2,pin3,pin4], 15)
	motor.move_to(180)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	
	mFL = multiprocessing.Process(target=createMotor, args=( 8,10,12,16,1))
	mFL.start()
	mFR = multiprocessing.Process(target=createMotor, args=(18,22,24,26,2))
	mFR.start()
	mBL = multiprocessing.Process(target=createMotor, args=( 3, 5, 7,11,3))
	mBL.start()
	mBR = multiprocessing.Process(target=createMotor, args=(15,19,21,23,4))
	mBR.start()
		#mFL = MotorThread( 8, 10, 12, 16, 1)
		#mFR = MotorThread(18, 22, 24, 26, 2)
		#mBL = MotorThread( 3,  5,  7, 11, 3)
		#mBR = MotorThread(15, 19, 21, 23, 4)


	try:
		pass
		#mFL = MotorThread( 8, 10, 12, 16, 1)
		#mFR = MotorThread(18, 22, 24, 26, 2)
		#mBL = MotorThread( 3,  5,  7, 11, 3)
		#mBR = MotorThread(15, 19, 21, 23, 4)

		#mFL.start()
		#mFR.start()
		#mBL.start()
		#mBR.start()


	except Exception as inst:
		print("Error: unable to start thread")
		print(type(inst))
		print(inst.args)
		print(inst)

	while True:
		pass

	GPIO.cleanup()

