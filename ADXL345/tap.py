from i2clibraries import i2c_adxl345
from time import *

adxl345 = i2c_adxl345.i2c_adxl345(1)

adxl345.setTapAxes(adxl345.TA_TapZAxis)
adxl345.setInterrupt(adxl345.SingleTap, adxl345.DoubleTap)

while True:
        # Determine if interrupt set
        [dataready, singletap, doubletap, activity, inactivity, freefall, watermark, overrun] = adxl345.getInterruptStatus()
        
        if doubletap:
                print("Double Tap")
        elif singletap:
                print("Single Tap")
