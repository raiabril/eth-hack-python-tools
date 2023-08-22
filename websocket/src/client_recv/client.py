import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"  # Change to the WebSocket server URI
    
    async with websockets.connect(uri) as websocket:
        # Receive and print the greeting from the server
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(hello())