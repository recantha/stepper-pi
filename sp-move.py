#!/usr/bin/env python
 
# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.
 
# It works on the Raspberry Pi computer with the standard Debian Wheezy OS and
# the 28BJY-48 stepper motor with ULN2003 control board.
 
from time import sleep
import RPi.GPIO as GPIO
 
class Motor(object):
    def __init__(self, pins):
        self.P1 = pins[0]
        self.P2 = pins[1]
        self.P3 = pins[2]
        self.P4 = pins[3]
        self.deg_per_step = 5.625 / 64
        self.steps_per_rev = int(360 / self.deg_per_step)  # 4096
        self.step_angle = 0  # Assume the way it is pointing is zero degrees
        for p in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, 0)
 
    def _set_rpm(self, rpm):
        """Set the turn speed in RPM."""
        self._rpm = rpm
        # T is the amount of time to stop between signals
        self._T = (60.0 / rpm) / self.steps_per_rev
 
    # This means you can set "rpm" as if it is an attribute and
    # behind the scenes it sets the _T attribute
    rpm = property(lambda self: self._rpm, _set_rpm)
 
    def move_to(self, angle):
        """Take the shortest route to a particular angle (degrees)."""
        # Make sure there is a 1:1 mapping between angle and stepper angle
        target_step_angle = 8 * (int(angle / self.deg_per_step) / 8)
        steps = target_step_angle - self.step_angle
        steps = (steps % self.steps_per_rev)
        if steps > self.steps_per_rev / 2:
            steps -= self.steps_per_rev
            print "moving " + `steps` + " steps"
            self._move_acw(-steps / 8)
        else:
            print "moving " + `steps` + " steps"
            self._move_cw(steps / 8)
        self.step_angle = target_step_angle
 
    def _move_acw(self, big_steps):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)
        for i in range(big_steps):
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)
 
    def _move_cw(self, big_steps):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)
        for i in range(big_steps):
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)
 
if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    m = Motor([18,22,24,26])
    m.rpm = 5
    print "Pause in seconds: " + `m._T`
    m.move_to(90)
    sleep(1)
    m.move_to(0)
    sleep(1)
    m.move_to(-90)
    sleep(1)
    m.move_to(-180)
    sleep(1)
    m.move_to(0)
    GPIO.cleanup()
