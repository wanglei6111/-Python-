树莓派二维码识别
===========================
你需要一块树莓派和原装摄像头
****
|Author|王磊|
|---|---
|E-mail|wanglei6111@gmail.com


使用
===============================
首先导入库zbarlight和PIL等库。<br>
然后复制代码：
***
摄像头：
```
camera = PiCamera()
camera.start_preview()                      #启动摄像头
sleep(0.5)                                  #预热并对焦
camera.capture('/home/pi/Desktop/cc.png')   #储存捕捉的图像
camera.stop_preview()
```
图像识别：
```
img = Image.open("/home/pi/Desktop/cc.png") #打开捕捉的图像
img.show()                                 

file_path = '/home/pi/Desktop/cc.png'
with open(file_path, 'rb') as image_file:   #加载捕捉的图像
    image = Image.open(image_file)
    image.load()

codes = zbarlight.scan_codes('qrcode', image) #解析二维码并打印
print('QR codes: %s' % codes)
```
图像流处理：
```
stream=io.BytesIO()                    #使用io
  with picamera.PiCamera() as camera:
      camera.start_preview()
      sleep(2)                         #两秒做对焦最低0.2
      camera.capture(stream,format="jpeg") #获得jpeg照片流
      stream.seek(0)                       #将流指针指向初始端           
      image=Image.open(stream)             
      codes = zbarlight.scan_codes('qrcode', image)
    print('QR codes: %s' % codes)
```
网络请求：
```
apiurl = '你的网址'
apiheaders = {'U-ApiKey': '你的key'}
response = requests.get(apiurl,params={"key1": 'value1', "key2": value2...}) #get方法请求对应的参数  
temp = response.json()  #json返回值  
print(temp)
code=temp['code']
print(code)
```
蜂鸣器及继电器等：
```
GPIO.setwarnings(False)  
PIN_NO = 13 #GPIO编号，可自定义  
PIN_aa=11   #GPIO编号，可自定义
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(PIN_NO, GPIO.OUT)  
GPIO.setup(PIN_aa, GPIO.OUT)
GPIO.output(PIN_aa, GPIO.HIGH)
```
