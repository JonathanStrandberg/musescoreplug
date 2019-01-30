import asyncio
from threading import Thread
import websockets
from socket import *

IPADS = set()
sender = None

def read_in_chunks(infile, chunk_size=1024*64):
    while True:
        chunk = infile.read(chunk_size)
        if chunk:
            yield chunk
        else:
            # The chunk was empty, which means we're at the end
            # of the file
            return


async def send_file():
    print('in sendfile')
    with open('new.pdf', 'rb') as pdf_file:
        #await websocket.send(read_in_chunks(pdf_file))
        print('try to send som data')
        #if IPADS:
            # await asyncio.wait([user.send(read_in_chunks(pdf_file)) for user in IPADS])
        buffer = pdf_file.read()
        if IPADS:
            await asyncio.wait([user.send(buffer) for user in IPADS])

def respond_to_any():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', 9876))
    while(True):
        print('before recv')
        (data, address) = s.recvfrom(1024)
        print('Received data from udp')
        s.sendto('thank you'.encode(), address)

async def echo(websocket, path):
    print('waiting in echo')
    async for message in websocket:
        print(message)
        if message == 'update':
            await send_file()
        else:
            IPADS.add(websocket)

Thread(target = respond_to_any).start()
print('after thread')
asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, port=8764))

asyncio.get_event_loop().run_forever()

