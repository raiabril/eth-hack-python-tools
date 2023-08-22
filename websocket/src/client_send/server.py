import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            # Receive a message from the client
            print(f"Received message from client: {message}")
            
            # Send a response back to the client
            response = f"Server received: {message}"
            await websocket.send(response)
            print(f"Sent response to client: {response}")
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
