import _thread
import utime

from machine import Pin
import LightController as lc
from getDetect import getDetect
import prexcp as p
import lcd

RED_NS = 21
YLW_NS = 20
GRN_NS = 19

RED_EW = 18
YLW_EW = 17
GRN_EW = 16

lc.AllOff(RED_NS, YLW_NS, GRN_NS)
lc.AllOff(RED_EW, YLW_EW, GRN_EW)

lc.TurnRed(RED_NS, YLW_NS, GRN_NS)
lc.TurnRed(RED_EW, YLW_EW, GRN_EW)

waiting_cars = {"NS": 0, "EW": 0}
car_detected_NS = False
car_detected_EW = False

# interrupts
def car_detected_NS(Pin):
    global car_detected_NS
    car_detected_NS = True
    
def car_detected_EW(Pin):
    global car_detected_EW
    car_detected_EW = True
    
    
# NS_digital = Pin(0, Pin.OUT)
# EW_digital = Pin(1, Pin.OUT)

# NS_digital.value(0)
# EW_digital.value(0)

# NS_interrupt = Pin(6, Pin.IN)
# EW_interrupt = Pin(7, Pin.IN)

# NS_interrupt.irq(trigger=Pin.IRQ_RISING, handler=car_detected_NS)
# EW_interrupt.irq(trigger=Pin.IRQ_RISING, handler=car_detected_EW)

SINGLE_GREEN_TIME = 3


def count_cars():
    while True:
        global NS_digital
        global EW_digital
        global waiting_cars
        
        north_detect, d = getDetect(15, 28)
        south_detect, d = getDetect(15, 27)
        east_detect, d  = getDetect(15, 26)
        
        # print(north_detect, south_detect, east_detect)
        
        if north_detect or south_detect:
            # NS_digital.value(1)
            waiting_cars["NS"] += 1
            print(f"\tNS detected car. {waiting_cars["NS"]} waiting.")
            lcd.lcdprint(0,0,f"\tNS detected car. {waiting_cars["NS"]} waiting.")
        if east_detect:
            # EW_digital.value(1)
            waiting_cars["EW"] += 1
            print(f"\tEW detected car. {waiting_cars["EW"]} waiting.")
            lcd.lcdprint(0,0,f"\tEW detected car. {waiting_cars["EW"]} waiting.")
_thread.start_new_thread(count_cars, ())
    
try:
    while True:  # main loop
        #if car_detected_NS:
         #   NS_digital.value(0)
          #  car_detected_NS = False
        #if car_detected_EW:
         #   EW_digital.value(0)
          #  car_detected_EW = False
        
        #print(waiting_cars)
        
        if waiting_cars["NS"]:
            cars_allowed = waiting_cars["NS"]
            print(f"\nletting {cars_allowed} cars through NS lights. -> green for {SINGLE_GREEN_TIME * cars_allowed} seconds.\n")
            lcd.lcdprint(0,0,f"\nletting {cars_allowed} cars through NS lights. -> green for {SINGLE_GREEN_TIME * cars_allowed} seconds.\n")
            waiting_cars["NS"] = 0
            utime.sleep(1)
            lc.TurnGreen(RED_NS, YLW_NS, GRN_NS)
            utime.sleep(SINGLE_GREEN_TIME * cars_allowed)
            lc.TurnRed(RED_NS, YLW_NS, GRN_NS)
        
        if waiting_cars["EW"]:
            cars_allowed = waiting_cars["EW"]
            print(f"\nletting {cars_allowed} cars through EW lights -> green for {SINGLE_GREEN_TIME * cars_allowed} seconds.\n")
            lcd.lcdprint(0,0,f"\nletting {cars_allowed} cars through EW lights -> green for {SINGLE_GREEN_TIME * cars_allowed} seconds.\n") 
            waiting_cars["EW"] = 0
            utime.sleep(1)
            lc.TurnGreen(RED_EW, YLW_EW, GRN_EW)
            utime.sleep(SINGLE_GREEN_TIME * cars_allowed)
            lc.TurnRed(RED_EW, YLW_EW, GRN_EW)
        
        utime.sleep(3)
except Exception as e:
    Pin(25, Pin.OUT).value(1)
    p.print_exc(e)


