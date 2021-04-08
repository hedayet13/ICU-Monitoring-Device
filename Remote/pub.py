import paho.mqtt.publish as publish
import time 

# start = time.time()

MQTT_SERVER = "********"  #Write Server IP Address
MQTT_PATH = "**********"
x=0
while True:
    start = time.time()
    f=open("img/res0.jpg", "rb") 
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)
    end =time.time()
    print(end-start)
    x+=1

# f=open("img/res2.jpg", "rb") #3.7kiB in same folder
# fileContent = f.read()
# byteArr = bytearray(fileContent)
# publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)
# totalTime = time.time()-start
# print('Done at ',totalTime)