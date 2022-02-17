import os
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',125)
engine.setProperty('voice','english+f3')
text='Hi!, I am BLINDA'
engine.say(text)
engine.runAndWait()
