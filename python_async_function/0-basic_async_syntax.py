#!/usr/bin/env python3
"""A module with a asynchronus routine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: _description_.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
