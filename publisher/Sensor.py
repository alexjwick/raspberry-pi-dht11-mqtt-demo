import Adafruit_DHT

class Sensor:
	def __init__(self, sensor, GPIO_pin):
		self.sensor = sensor
		self.GPIO_pin = GPIO_pin

	def get_reading(self):
		humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.GPIO_pin)
		if humidity is not None and temperature is not None:
			return humidity, temperature
		raise NullSensorReadingException('Failed to get reading. Try again!')

class NullSensorReadingException(Exception):
	pass

if __name__ == '__main__':
	sensor = Adafruit_DHT.DHT11

	# Set GPIO_pin to the pin that is connected to the DHT11 sensor's data pin
	GPIO_pin = 4

	sensor = Sensor(sensor, GPIO_pin)
	try:
		humidity, temperature = sensor.get_reading()
		print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
	except NullSensorReadingException as e:
		print(e)