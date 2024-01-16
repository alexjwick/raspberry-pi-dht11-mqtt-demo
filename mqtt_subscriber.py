import paho.mqtt.client as paho
import time

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = paho.Client()
client.on_message = message_handling

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    exit(1)

datetime = time.strftime("%Y-%m-%d %H:%M:%S")
print("Connected to the MQTT broker at {0}".format(datetime))
client.subscribe("sensor")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except KeyboardInterrupt:
    print("KeyboardInterrupt, exiting...")
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
