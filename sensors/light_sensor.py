# -*- coding: utf-8 -*-

import smbus
import time

# Constants from datasheet
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20

# Initializing i2c port via smbus
bus = smbus.SMBus(1) 
 
def toNumber(data):
  return (256 * data[0] + data[1]) / 1.2
 
def readLight(dev_address=DEVICE):
  data = bus.read_i2c_block_data(dev_address, 0x20)
  return round(toNumber(data), 2)
 
def main():
  
  while True:
      with open('/home/pi/Desktop/data/data/bh1750_light_sensor.txt', 'a') as f:
          f.write("{\"id\":1, \"time\":" + str(int(time.time())) + ",\"lux\":" + str(readLight()) + "}\n")
          time.sleep(1)
 
if __name__=="__main__":
   main()
