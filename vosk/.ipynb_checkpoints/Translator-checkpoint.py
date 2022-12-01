import asyncio
import websockets
import sys
import wave
import json

async def transmit_file(filename: str = "", url: str = "wss://vosk.chompe.rs"):

    async with websockets.connect(url) as ws:

        wav = wave.open(filename, "rb")

        await ws.send(
            '{"config": {"sample_rate": %d }}' % (wav.getframerate())
        )

        buffer = 6400

        while True:
            data = wav.readframes(buffer)

            if len(data) == 0:
                break

            await ws.send(data)

            response = json.loads(await ws.recv())
            if "text" in response.keys():
                return response["text"]

        await ws.send('{"eof": 1}')

def transcribe(filename: str = "") -> str:
    text = asyncio.run(transmit_file(filename))
    return text
