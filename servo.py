from servoDriver import Servo
from machine import Pin
import time

try:
    servo = Servo(12)
    servo.ServoAngle(0)
    TIME_STEP = 25

    btn = Pin(13, Pin.IN, Pin.PULL_UP)

    arm_lowered = False
except Exception as e:
    for _ in range(3):
        Pin(25, Pin.OUT).value(1)
        time.sleep(0.3)
        Pin(25, Pin.OUT).value(0)
        time.sleep(0.3)
    print(e)


def lower_arm():
    global arm_lowered
    
    for i in range(0, 90, 1):
        servo.ServoAngle(i)
        time.sleep_ms(TIME_STEP)
    arm_lowered = True
    time.sleep_ms(20)


def raise_arm():
    global arm_lowered
    
    for i in range(90, 0, -1):
        servo.ServoAngle(i)
        time.sleep_ms(TIME_STEP)
    arm_lowered = False
    time.sleep_ms(20)
            
            
def change_arm():
    if not arm_lowered:
        print("lowering arm")
        lower_arm()
    elif arm_lowered:
        print("raising arm")
        raise_arm()
        
def button_change():
    if not btn.value():
        time.sleep_ms(20)
        if not btn.value():
            change_arm()
            while not btn.value():
                time.sleep_ms(20)

if __name__ == "__main__":
    try:
        while True:
            if not btn.value():
                time.sleep_ms(20)
                if not btn.value():
                    change_arm()
                    
                    while not btn.value():
                        time.sleep_ms(20)
    except Exception as e:
        servo.deinit()
        for _ in range(10):
            Pin(25, Pin.OUT).value(1)
            time.sleep(0.3)
            Pin(25, Pin.OUT).value(0)
            time.sleep(0.3)
        print(e)
        
        
