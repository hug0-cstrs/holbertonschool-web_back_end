#!/usr/bin/env python3
"""A module with two concurrent routines"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function executing multiple coroutines"""
    task_list = []
    for _ in range(n):
        task_list.append(task_wait_random(max_delay))
    results = await asyncio.gather(*task_list)
    return sorted(results)
