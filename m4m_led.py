# -*- coding: utf-8 -*-
import sys, time
import RPi.GPIO as GPIO

redPin   = 11
greenPin = 13
bluePin  = 15

def blink(pin):
	1+1
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(pin, GPIO.OUT)
    #GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
	1+1
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(pin, GPIO.OUT)
    #GPIO.output(pin, GPIO.LOW)

def redOn():
	blink(redPin)

def greenOn():
    blink(greenPin)

def blueOn():
    blink(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def redOff():
    turnOff(redPin)

def greenOff():
    turnOff(greenPin)

def blueOff():
    turnOff(bluePin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)