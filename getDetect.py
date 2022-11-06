from machine import Pin, ADC, PWM

import time


def getDetect(p,a):

    pwm = PWM(Pin(p))
    adc = ADC(a)
    

    pwm.duty_u16(adc.read_u16())
    time.sleep(0.5)
        
    if pwm.duty_u16() < 600:
        return False
    else:
        return True


if __name__ == "__main__":
    while True:
        print(getDetect(15,28))
        time.sleep(0.5)
