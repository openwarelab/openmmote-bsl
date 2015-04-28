#!/usr/bin/python

import os
import serial
import subprocess
import sys
import time

High = True
Low  = False

cc2538_bsl_path = "cc2538-bsl"
cc2538_bsl_name = "cc2538-bsl.py"
cc2538_bsl_params = ['-e', '-w', '-b 115200', '--bsl']

def bsl_init(ser):
    pass

def bsl_start(ser):
    ser.setDTR(High)
    time.sleep(0.5)
    ser.setRTS(Low)
    time.sleep(0.5)
    ser.setDTR(Low)
       
def bsl_flash(arguments):
    script = [os.path.join(cc2538_bsl_path, cc2538_bsl_name)] + cc2538_bsl_params + arguments
    process = subprocess.call(script, shell=False)
    
def bsl_open():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    bsl_start(ser)
    while(True):
        line = ser.readline()
        print line
    bsl_stop(ser)
     
def bsl_stop(ser):
    ser.setDTR(High)
    time.sleep(0.5)
    ser.setRTS(Low)
    time.sleep(0.5)
    ser.setDTR(Low)

def parse_args(args):
    if '-f' in args:
        bsl_flash(args[1:])
    elif '-o' in args:
        bsl_open()
    else:
        print('Argument error! Use: ')
        print('\topenusb-bsl.py -f test.hex to flash')
        print('\topenusb-bsl.py -o to open serial port')

def main(argv):
    args = parse_args(argv[1:])

if __name__ == "__main__":
    main(sys.argv)
