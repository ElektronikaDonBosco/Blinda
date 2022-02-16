import jetson.inference
import jetson.utils
import numpy as np
import os
from gtts import gTTS
import threading

speak=True
item='Hello!, I am Blinda'
confidence=0
itemOld=''

def sayItem():
    global speak
    global item
    while True:
        if speak==True:
            output=gTTS(text=item, lang='en', slow=False)
            output.save('output.mp3')
            os.system('mpg123 output.mp3')
            speak=False

x=threading.Thread(target=sayItem, daemon=True)
x.start()

net=jetson.inference.imageNet('googlenet')
camera=jetson.utils.gstCamera(480,360, 'csi://0')
display=jetson.utils.glDisplay()

while display.IsOpen():
    img, width, height = camera.CaptureRGBA()
    if speak==False:         
        classID, confidence = net.Classify(img, width, height)
        if confidence>=.5:
            item = net.GetClassDesc(classID)
            print(item)
            if item!=itemOld:
                speak=True
        if confidence<.5:
            item=''
        itemOld=item
      
camera.Close()
 