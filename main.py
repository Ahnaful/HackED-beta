import time

import LightController as lc

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
    time.sleep(1)
    lc.TurnGreen(RED_NS, YLW_NS, GRN_NS)
    time.sleep(3)
    lc.TurnRed(RED_NS, YLW_NS, GRN_NS)
    
    time.sleep(1)
    lc.TurnGreen(RED_EW, YLW_EW, GRN_EW)
    time.sleep(3)
    lc.TurnRed(RED_EW, YLW_EW, GRN_EW)
    