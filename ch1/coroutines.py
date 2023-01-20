#coroutines.py
import asyncio
import time
async def main():
    for i in range(1,6):
        await myfunction(i)
        print ('In main', i)

async def myfunction(i):
    print ('In myfunction', i)
    time.sleep(2)

asyncio.run(main())
