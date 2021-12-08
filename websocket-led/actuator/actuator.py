import asyncio
import websockets
import json
import os

import RPi.GPIO as GPIO


URL = 'ws://'+os.environ['IP']+':7890'
STATE = False


async def client():
    try:
        async with websockets.connect(URL) as server:
            info = {}
            info['type'] = 'actuator'
            await server.send(json.dumps(info))
            while True:
                message = await server.recv()
                message = json.loads(message)
                print('Actuation : '+str(message['value']))
                global STATE
                if STATE:
                    GPIO.output(18, GPIO.LOW)
                    STATE = not STATE
                else:
                    GPIO.output(18, GPIO.HIGH)
                    STATE = not STATE

    except Exception as e:
        print(str(e))


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
asyncio.run(client())
