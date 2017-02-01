#!/usr/bin/python

'''
Made by Groguard and Zerocool5878 
1/31/17
Reset Switch goes in GPIO 24 and GND

'''

import RPi.GPIO as GPIO
import os
import socket
from time import sleep

ledPin = 14
fanPin = 18
shutdownPin = 3
resetPin = 24
fanOnTemp = 60

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(shutdownPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(fanPin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, GPIO.HIGH)

def retroPiCmd(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, ("127.0.0.1", 55355))

def btnCmds(channel):
    if channel == resetPin:
        retroPiCmd("QUIT")

def readCpuTemp():
    readTemp = os.popen('vcgencmd measure_temp').readline()
    return(readTemp[5:9])

GPIO.add_event_detect(resetPin, GPIO.FALLING, callback=btnCmds)

while True:
    temp = float(readCpuTemp())
    input_state = GPIO.input(shutdownPin)
    if temp > fanOnTemp:
        GPIO.output(fanPin, GPIO.HIGH)
    if temp < fanOnTemp:
        GPIO.output(fanPin, GPIO.LOW)
    if input_state == True:
        GPIO.output(ledPin, GPIO.LOW)
        sleep(0.25)
        GPIO.output(ledPin, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(ledPin, GPIO.LOW)
        sleep(0.25)
        GPIO.output(ledPin, GPIO.HIGH)
        os.system("sudo shutdown -h now")
    sleep(0.5)
    
    
