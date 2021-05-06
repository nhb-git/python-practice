import asyncio
import time


async def mul(first, second):
    """ ... """
    print(f"Calculating multiply of {first} and {second}")
    await asyncio.sleep(1)
    num_mul = first * second
    print(f"Multiply of {num_mul}")
    return num_mul


async def sum(first, second):
    """ ... """
    print(f"Calculating sum of {first} and {second}")
    await asyncio.sleep(1)
    num_sum = first + second
    print(f"Sum is {num_sum}")
    return num_sum


async def main(first, second):
    """ ... """
    start = time.perf_counter()
    sum_task = asyncio.get_event_loop().create_task(sum(first, second))
    mul_task = asyncio.get_event_loop().create_task(mul(first, second))
    await sum_task
    await mul_task
    end = time.perf_counter()
    print(f"total time: {end-start}")


asyncio.get_event_loop().run_until_complete(main(7, 8))
