from machine import Pin
import time

def RedtoGreen(r, g):

    redPin = Pin(r, Pin.OUT)
    greenPin = Pin(g, Pin.OUT)

    redPin.value(0)
    greenPin.value(1)

def GreentoRed(r,y,g):

    redPin = Pin(r, Pin.OUT)
    yellowPin = Pin(y, Pin.OUT)
    greenPin = Pin(g, Pin.OUT)

    greenPin.value(0)
    yellowPin.value(1)
    time.sleep(3)
    yellowPin.value(0)
    redPin.value(1)
    

def AllOff(r, y, g):
    Pin(r, Pin.OUT).value(0)
    Pin(y, Pin.OUT).value(0)
    Pin(g, Pin.OUT).value(0)