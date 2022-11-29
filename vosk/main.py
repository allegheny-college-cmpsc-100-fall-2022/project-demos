import asyncio
import websockets
import sys
import wave

async def transmit_file(url: string = "https://vosk.chompe.rs"):
    async with websockets.connect(url) as ws:
        wav = wave.open("QuickFox.wav")
        await websocket.send(
            '{"config": {"sample_rate": f"{wav.getframerate()}"}}'
        )
        buffer = 6400
        while True:
            data = wav.readframes(buffer)
            if len(data) == 0:
                break
            await websocket.send(data)
            print(await websocket.recv())
        await websocket.send('{"eof": 1}')
        print(await websocket.recv())
asyncio.run(transmit_file())