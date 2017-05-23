# -*- coding: utf-8 -*-

import os
import subprocess
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0415a25409ff/w1_slave'


def readTemp(celsius=True):
    temp = None
    req = 'cat %s' % (temp_sensor)
    s = subprocess.check_output(req, shell=True).strip()
    lines = s.split('\n')
    if lines[0].split(' ')[-1] == 'YES':
        temp = float(lines[1].split(' ')[-1].split('=')[-1])/1000
    
    if celsius:
        return temp
    else:
        return temp*9/5 + 32


if __name__ == '__main__':
    while True:
        print(readTemp())
        time.sleep(1)

