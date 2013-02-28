stepper-pi
==========

Scripts to control stepper motors from the Raspberry Pi over GPIO
These scripts are for a ULN2003 control board running a 5V 28BJY-48 motor

#########################################################################

Stepper.py - class to control a stepper motor, based on work by Stephen C Phillips

test-all-motors.sh - runs test-motor.py 4 times - one for each motor

test-motor.py - tests a single motor, given the 4 GPIO pins it is connected to

sp-move.py - Stephen C Phillips' original script incorporating class-based control of a stepper motor. www.scphillips.com

mh-stepper.py - Matt Hawkins script to control a stepper, which doesn't work for me, probably because of a change in the GPIO library
