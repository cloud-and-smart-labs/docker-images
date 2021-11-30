import RPi.GPIO as GPIO
from urllib.request import urlopen
import time
import json
import os

def get_delay(URL):
    with urlopen(URL) as url:
        data = json.loads(url.read().decode())
        return data['delay']

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
URL = 'http://'+os.environ['IP']+'/delay'
# URL = 'http://192.168.0.222/delay'

try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(get_delay(URL))
        GPIO.output(18, GPIO.LOW)
        time.sleep(get_delay(URL))
except Exception as e:
    print (str(e))
finally:
    GPIO.cleanup()