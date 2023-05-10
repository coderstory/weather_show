from machine import Pin
import time

led = Pin(2, Pin.OUT)

# 蓝色LED闪烁

while True:
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
