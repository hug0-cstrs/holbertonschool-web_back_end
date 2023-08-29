#!/usr/bin/env python3
"""A module with a asynchronus routine"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous function that launches the wait_random function 'n'
    times with the specified maximum delay.

    Args:
        n (int): The number of times to launch the wait_random function.
        max_delay (int): The maximum delay for each call to wait_random.

    Returns:
        list: A list of all the delays (floating-point values)
        in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = await asyncio.gather(*tasks)
    delays.sort()

    return delays
