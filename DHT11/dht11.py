import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
print(humidity, temperature)
