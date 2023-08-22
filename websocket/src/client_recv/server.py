import asyncio
import websockets

async def hello(websocket, path):
    # This function will be called whenever a new WebSocket connection is established.
    # 'websocket' is the WebSocket connection object.
    # 'path' is the path requested by the client (not used in this example).
    
    # Send a greeting to the client
    await websocket.send("Hello, World!")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()