from machine import Pin
import onewire, ds18x20
import time
 
 
ds_sensor = ds18x20.DS18X20(onewire.OneWire(Pin(13)))
 

def read_ds_sensor():  # 创建一个读取温度的函数
    roms = ds_sensor.scan()  # 扫描总线上的设备
    print('扫描发现的设备: ', roms)
    ds_sensor.convert_temp()  # 温度转换
    for rom in roms:  # 循环打印出设备列表
        temp = ds_sensor.read_temp(rom)  # 读出该设备的温度
        if isinstance(temp, float):  # 以小数点后2位输出，例如23.35
            temp = round(temp, 2)
            return temp
    return 0
 
 
while True:
    temp = read_ds_sensor()
    print(f'current temp is {temp}')
    if(temp < 25):
        print("温度低了，请开启加热器！")
    if(temp > 30):
        print("温度高了，请开启制冷器！")    
    time.sleep(1)
