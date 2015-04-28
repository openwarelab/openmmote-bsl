#!/usr/bin/python

import os
import serial
import subprocess
import sys
import time

import RPi.GPIO as gpio

cc2538_bsl_path = "cc2538-bsl"
cc2538_bsl_name = "cc2538-bsl.py"
cc2538_bsl_params = "-e -w -b 115200"

BSL   = 23
RESET = 24

HIGH = True
LOW  = False

def bsl_init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(BSL, gpio.OUT)
    gpio.setup(RESET, gpio.OUT)

def bsl_start():
    gpio.output(RESET, HIGH)
    gpio.output(BSL, HIGH)
    gpio.output(RESET, LOW)
    gpio.output(BSL, LOW)
    gpio.output(RESET, HIGH)
    
def bsl_flash(arguments):
    script = [os.path.join(cc2538_bsl_path, cc2538_bsl_name), cc2538_bsl_params] + arguments
    process = subprocess.call(script, shell=False)
    
def bsl_stop():
    gpio.output(RESET, LOW)
    gpio.output(BSL, HIGH)
    gpio.output(RESET, HIGH)

def main(argv):
    bsl_init()
    bsl_start()
    bsl_flash(argv[1:])
    bsl_stop()
    
if __name__ == "__main__":
    main(sys.argv)
