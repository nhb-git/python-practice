import asyncio
import time


async def hello(first_print, second_print):
    print(first_print)
    await asyncio.sleep(1)
    print(second_print)


async def main():
    print(f"Starting Tasks: {time.strftime('%X')}")
    task1 = asyncio.get_event_loop().create_task(hello('one', 'one_1'))
    task2 = asyncio.get_event_loop().create_task(hello('two', 'two_2'))
    await task1
    await task2
    print(f"Finished Tasks: {time.strftime('%X')}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
