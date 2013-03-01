#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys

import thread
import Queue


def run_motor(threadName, pin1, pin2, pin3, pin4):
	m = Motor([int(pin1), int(pin2), int(pin3), int(pin4)], 15)

	m.move_to(180)
	sleep(1)

def test_thread(threadName, tmp):
	while True:
		evt = q.get()
		print(evt[2])


if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)


	q = Queue.Queue(maxsize=0)
	thread.start_new_thread(test_thread, ("Receiver", 1))

	while True:
		evt = ("Hello world", "My name is bob", "her name is sheila")
		q.put(evt)
		sleep(0.5)

	exit(0)


	try:
		thread.start_new_thread(run_motor, ("Thread-FL", 8, 10, 12, 16))
		thread.start_new_thread(run_motor, ("Thread-FR",18, 22, 24, 26))
		thread.start_new_thread(run_motor, ("Thread-BL", 3,  5,  7, 11))
		thread.start_new_thread(run_motor, ("Thread-BR",15, 19, 21, 23))

	except:
		print "Error: unable to start thread"

	while True:
		pass

	GPIO.cleanup()

