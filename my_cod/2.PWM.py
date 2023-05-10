from machine import Pin,PWM   #这里是是2号引脚，也就是那个小灯泡，亮度逐渐增加，再减少，循环
import utime
 
LED=PWM(Pin(2))
 
LED.freq(1000)       #设置他的频率为1000HZ
 
LED_duty=0
LED_direction=1
 
while True:
    LED_duty+=LED_direction
    if LED_duty>=100:
        LED_duty=100
        LED_direction=-1
    elif LED_duty<=0:
        LED_duty=0
        LED_direction=1
    LED.duty_u16(int(LED_duty*655.35))   #改变占空比
    if LED_duty%5==0:
        print(LED_duty)       #打印LED_duty的值

    utime.sleep(0.01)     #休息100ms