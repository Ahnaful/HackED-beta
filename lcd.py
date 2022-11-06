import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

i2c = I2C(1, sda=Pin(10), scl=Pin(11), freq=400000)
devices = i2c.scan()

lcd = I2CLcd(i2c, devices[0], 2, 16)

def lcdprint(x, y, s, clear=True):
    if clear:
        lcd.clear()
    else:
        pass
    lcd.move_to(x, y)
    lcd.putstr(s)

if __name__ == "__main__": 
    lcdprint(0, 0, 'Cars', clear=True)