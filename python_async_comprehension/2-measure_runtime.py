#!/usr/bin/env python3
"""A module with a asynchronous generator"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of the async generator"""
    start = time.time() # Enregistre le temps de départ
    await asyncio.gather(*(async_comprehension() for i in range(4))) # Appelle async_comprehension 4 fois
    end = time.time() # Enregistre le temps de fin
    return end - start # Retourne le temps d'exécution total
