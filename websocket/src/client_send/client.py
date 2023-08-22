import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"  # Change to the WebSocket server URI

    async with websockets.connect(uri) as websocket:
        message = "Hello, Server!"
        print(f"Sending message to server: {message}")
        await websocket.send(message)

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
