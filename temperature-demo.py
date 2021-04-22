from sense_emu import SenseHat
from time import sleep

import paho.mqtt.client as mqtt

broker_ip = 'broker.hivemq.com'
broker_port = 1883
mqtt_topic = 'raspberry-iot/temperature'

#client.connect(broker_ip, broker_port, 60)

#def on_connect(client, obj, flags, rc):
    # self.master.subscribe(mqtt_topic)
    #print("connected" + str(mid))
    
#def on_publish(client, obj, mid):
    
client = mqtt.Client()
    
        
#def mqtt_pub(client, payload):
    
sense = SenseHat()


red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = round(sense.temp, 1)
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
    print("The temperature is" ,temp, "degrees")
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, temp)
    sleep(1)
    
    