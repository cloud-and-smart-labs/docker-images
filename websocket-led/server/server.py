import asyncio
import websockets
import json


PORT = 7890
HOST = '0.0.0.0'
actuators = set()

print('Listening to POST : ', str(PORT))


async def echo_server(client_websocket):
    print('Client conncted...')

    try:
        async for message in client_websocket:
            print('Received message : '+str(message))
            message = json.loads(message)

            if message['type'] == 'actuator':
                actuators.add(client_websocket)

            if message['type'] == 'control' and actuators:
                print('< actuation >')
                actuation = {}
                actuation['type'] = 'actuation'
                actuation['value'] = message['value']
                websockets.broadcast(actuators, json.dumps(actuation))

    except Exception as e:
        print(str(e))
    finally:
        if client_websocket in actuators:
            actuators.remove(client_websocket)


async def server():
    async with websockets.serve(echo_server, HOST, PORT):
        await asyncio.Future()  # Run forever

asyncio.run(server())
