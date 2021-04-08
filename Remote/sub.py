import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "*****"
MQTT_PATH = "*********"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
    start = time.time()
    f = open('output.jpg', "wb")
    f.write(msg.payload)
    end = time.time()
    res= end -start
    print("Image Received:",res)

    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
end = time.time()
# print(end-start)
client.loop_forever()