import time

import LightController as lc
from getDetect import getDetect

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

while True:  # main loop
    north_detect = getDetect(15, 28)
    south_detect = getDetect(15, 27)
    east_detect  = getDetect(15, 26)
    
    print(north_detect, south_detect, east_detect)
    
    if north_detect or south_detect:
        time.sleep(1)
        lc.TurnGreen(RED_NS, YLW_NS, GRN_NS)
        time.sleep(5)
        lc.TurnRed(RED_NS, YLW_NS, GRN_NS)
    
    if east_detect:
        time.sleep(1)
        lc.TurnGreen(RED_EW, YLW_EW, GRN_EW)
        time.sleep(5)
        lc.TurnRed(RED_EW, YLW_EW, GRN_EW)
    