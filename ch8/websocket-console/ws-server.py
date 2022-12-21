import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

server = websockets.serve(hello, 'localhost', 8765)

loop=asyncio.get_event_loop()
loop.run_until_complete(server)
loop.run_forever()

