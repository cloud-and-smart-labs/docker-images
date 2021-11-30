import RPi.GPIO as GPIO
from urllib.request import urlopen
import time
import json
import os


def get_delay(URL):
    with urlopen(URL) as url:
        data = json.loads(url.read().decode())
        return data['delay']


pin = 18
URL = 'http://'+os.environ['IP']+'/delay'
#URL = 'http://192.168.0.112/delay'

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(get_delay(URL))
        GPIO.output(pin, GPIO.LOW)
        time.sleep(get_delay(URL))
except Exception as e:
    print (str(e))
    GPIO.output(pin, GPIO.LOW)
finally:
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()