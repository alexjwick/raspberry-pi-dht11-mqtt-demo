import paho.mqtt.client as paho
import Adafruit_DHT
import time
from Sensor import Sensor

sensor = Sensor(Adafruit_DHT.DHT11, 4)

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    exit(1)

while True:
    try:
        humidity, temperature = sensor.get_reading()
        datetime = time.strftime("%Y-%m-%d %H:%M:%S")
        message = "{0} Temp: {1:0.1f}*C Humidity: {2:0.1f}%".format(datetime, temperature, humidity)
        print(message)
        client.publish("sensor", message)
        time.sleep(5)
    except KeyboardInterrupt:
        print("KeyboardInterrupt, exiting...")
        break
    except Exception as e:
        print(e)
        break
client.disconnect()