树莓派二维码识别
===========================
你需要一块树莓派和原装摄像头
****
|Author|王磊|
|---|---
|E-mail|wanglei6111@gmail.com


===============================

使用
===============================
首先导入库zbarlight和PIL。<br>
然后复制代码：
***
要引入的：
***
```
#-*- coding: UTF-8 -*-
import time
import picamera
import logging
import random
import zbarlight
from PIL import Image
from picamera import PiCamera
from time import sleep
```
camera = PiCamera()
camera.start_preview()                      #启动摄像头
sleep(0.5)                                  #预热并对焦
camera.capture('/home/pi/Desktop/cc.png')   #储存捕捉的图像
camera.stop_preview()

img = Image.open("/home/pi/Desktop/cc.png") #打开捕捉的图像
img.show()                                 

file_path = '/home/pi/Desktop/cc.png'
with open(file_path, 'rb') as image_file:   #加载捕捉的图像
    image = Image.open(image_file)
    image.load()

codes = zbarlight.scan_codes('qrcode', image) #解析二维码并打印
print('QR codes: %s' % codes)

