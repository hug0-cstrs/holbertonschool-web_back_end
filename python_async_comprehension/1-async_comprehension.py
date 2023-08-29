#!/usr/bin/env python3
"""A module with a asynchronous generator"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Coroutine collects 10 random numbers using asynchronous understanding"""
    random_numbers = [num async for num in async_generator()]
    return random_numbers
