import aiohttp
import asyncio

async def main():
    while(True):
        async with aiohttp.ClientSession() as session:
              
              async with session.get('http://127.0.0.1:80') as response:
                  pass

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
asyncio.run(main())
