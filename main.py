import _thread
import utime

from machine import Pin
import LightController as lc
from getDetect import getDetect
import prexcp as p

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
    
    
NS_digital = Pin(0, Pin.OUT)
EW_digital = Pin(1, Pin.OUT)

NS_digital.value(0)
EW_digital.value(0)

NS_interrupt = Pin(6, Pin.IN)
EW_interrupt = Pin(7, Pin.IN)

NS_interrupt.irq(trigger=Pin.IRQ_RISING, handler=car_detected_NS)
EW_interrupt.irq(trigger=Pin.IRQ_RISING, handler=car_detected_EW)


def count_cars():
    while True:
        global NS_digital
        global EW_digital
        global waiting_cars
        
        north_detect = getDetect(15, 28)
        south_detect = getDetect(15, 27)
        east_detect  = getDetect(15, 26)
        
        # print(north_detect, south_detect, east_detect)
        
        if north_detect or south_detect:
            NS_digital.value(1)
        
        if east_detect:
            EW_digital.value(1)
            
_thread.start_new_thread(count_cars, ())
    
try:
    while True:  # main loop
        if car_detected_NS:
            print("NS")
            NS_digital.value(0)
            car_detected_NS = False
        if car_detected_EW:
            print("EW")
            EW_digital.value(0)
            car_detected_EW = False
        
        if waiting_cars["NS"]:
            utime.sleep(1)
            lc.TurnGreen(RED_NS, YLW_NS, GRN_NS)
            utime.sleep(3 * waiting_cars["NS"])
            waiting_cars["NS"] = 0
            lc.TurnRed(RED_NS, YLW_NS, GRN_NS)
        
        if waiting_cars["EW"]:
            utime.sleep(1)
            lc.TurnGreen(RED_EW, YLW_EW, GRN_EW)
            utime.sleep(3 * waiting_cars["EW"])
            waiting_cars["EW"] = 0
            lc.TurnRed(RED_EW, YLW_EW, GRN_EW)
        
        utime.sleep(0.1)
except Exception as e:
    Pin(25, Pin.OUT).value(1)
    p.print_exc(e)
