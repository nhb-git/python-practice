import asyncio
import time


async def greetings():
    """ ... """
    print("Welcome")
    await asyncio.sleep(1)
    print("Good by")


async def main():
    await asyncio.gather(greetings(), greetings())


def say_greet():
    start = time.perf_counter()
    asyncio.get_event_loop().run_until_complete(main())
    elapsed = time.perf_counter() - start
    print(f"total time elapsed: {elapsed}")


asyncio.get_event_loop().run_until_complete(say_greet())
