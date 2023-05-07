# 蜂鸣器实验

# ESP32 - 电机模块(ULN2003D) - 蜂鸣器

from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
if __name__ == "__main__":
    value = True
    while True:
        value = not value
        led.value(value)
        sleep(1)
