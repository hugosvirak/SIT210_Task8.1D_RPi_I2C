# NOTE: Heavily inspired from https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bh1750.py

#!/usr/bin/python

import smbus # a library to read or write from the system management bus
import time

LightSensorAddress     = 0x23

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

bus = smbus.SMBus(1)

def getIntensity():
  # Read data from I2C interface
  data = bus.read_i2c_block_data(LightSensorAddress,ONE_TIME_HIGH_RES_MODE_1) # read light value from the address
  return (data[1] + (256 * data[0])) / 1.2 # convert from byte to number and return that value
   
 
while True:
    lightLevel=getIntensity()
    if (lightLevel > 1000):
        print ("too bright")
    elif (lightLevel > 600):
        print ("bright")
    elif (lightLevel > 100):
        print ("medium")
    elif (lightLevel > 50):
        print ("dark")
    else:
        print ("too dark")
    time.sleep(0.5)
