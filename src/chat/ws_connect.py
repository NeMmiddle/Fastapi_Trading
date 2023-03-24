import asyncio
import time

import aiohttp

"""An example of a WEBSocket for an intended chat with saving all user responses to a txt file"""
async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        async with session.ws_connect(
            f"http://localhost:8000/chat/ws/{client_id}"
        ) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")


asyncio.run(main())
