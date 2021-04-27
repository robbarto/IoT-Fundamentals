# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2021-04-16-09-32-11.py"

#import the correct libraries

from sense_emu import SenseHat

sense = SenseHat()

from time import sleep

import paho.mqtt.client as mqtt

broker_ip = 'broker.hivemq.com'
broker_port = 1883
mqtt_topic = 'raspberry-iot/humidity'

client = mqtt.Client()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    humidity_value = round(humidity_value,2)
    pixels = [green if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)
    print("The Humidity is" ,humidity_value, "%")
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, humidity_value)
    sleep(1)

