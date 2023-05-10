
# 连接wifi

import network
import time
import urequests
import gc

sta_if = network.WLAN(network.STA_IF);
 
sta_if.active(False)
sta_if.active(True)

sta_if.scan()                             
sta_if.connect("CODERSTORY-PC 4554", "123456789")

for i in range(10):
    if not sta_if.isconnected():
        time.sleep(1)
    else:
        break    
    
print(sta_if.status("rssi"))                     
 

response = urequests.get("https://blog.coderstory.cn/")
print(response.text)
gc.collect()