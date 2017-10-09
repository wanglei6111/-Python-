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
|---|---|----
|1|#-*- coding: UTF-8 -*-
|2|import time
|3||1|import picamera
|4|import logging
|5|import random
|6|import zbarlight
|1|from PIL import Image
|1|from picamera import PiCamera
|1|from time import sleep

|1|camera = PiCamera()
|1|camera.start_preview()                      #启动摄像头
|1|sleep(0.5)                                  #预热并对焦
|1|camera.capture('/home/pi/Desktop/cc.png')   #储存捕捉的图像
|1|camera.stop_preview()

|1|img = Image.open("/home/pi/Desktop/cc.png") #打开捕捉的图像
|1|img.show()                                 

|1|file_path = '/home/pi/Desktop/cc.png'
|1|with open(file_path, 'rb') as image_file:   #加载捕捉的图像
    image = Image.open(image_file)
    image.load()

|1|codes = zbarlight.scan_codes('qrcode', image) #解析二维码并打印
|1|print('QR codes: %s' % codes)

