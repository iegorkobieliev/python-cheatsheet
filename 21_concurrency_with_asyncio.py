import asyncio


async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)


asyncio.run(print_numbers())
