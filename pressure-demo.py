# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2021-04-16-09-32-11.py"

from sense_emu import SenseHat
import math

sense = SenseHat()

from time import sleep

import paho.mqtt.client as mqtt

broker_ip = 'broker.hivemq.com'
broker_port = 1883
mqtt_topic = 'raspberry-iot/pressure'

client = mqtt.Client()

yellow = (125, 125, 125)
white = (255, 255, 255)

while True:
    pressure = sense.pressure
    kpa_pressure = pressure/10
    kpa_pressure = round(kpa_pressure,2)
    #pixels = [green if i < humidity_value else white for i in range(64)]
    #sense.set_pixels(pixels)
    print("The Pressure is" ,kpa_pressure, "KPa")
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, str(kpa_pressure))
    sleep(1)

