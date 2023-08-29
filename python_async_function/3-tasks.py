#!/usr/bin/env python3
"""A module with a asynchronus routine"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns a task object"""
    task_wait_random_task = asyncio.create_task(wait_random(max_delay))

    return task_wait_random_task
