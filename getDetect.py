from machine import Pin, ADC, PWM

import time


def getDetect(pwm_pin, adc_pin):

    pwm = PWM(Pin(pwm_pin))
    adc = ADC(adc_pin)
    

    pwm.duty_u16(adc.read_u16())
    time.sleep(0.5)
        
    if pwm.duty_u16() < 600:
        return False, pwm.duty_u16()
    else:
        return True, pwm.duty_u16()


if __name__ == "__main__":
    while True:
        print("L: ", getDetect(15, 28))
        print("M: ", getDetect(15, 27))
        print("R: ", getDetect(15, 26))
        print()
        
        time.sleep(2)
