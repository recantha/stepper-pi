#!/usr/bin/python

from Stepper import Motor
from time import sleep
import RPi.GPIO as GPIO
import sys
import datetime
import subprocess

mFL = [ 8, 10, 12, 16]
mFR = [18, 22, 24, 26]
mBL = [ 3,  5,  7, 11]
mBR = [15, 19, 21, 23]

subprocess.call(["python trigger-motor.py " + str(mFL[1])])
