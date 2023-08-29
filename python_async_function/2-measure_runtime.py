#!/usr/bin/env python3
"""A module with a asynchronus routine"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total pour wait_n(n, max_delay)
    et retourne le temps moyen par appel.

    Args:
        n (int): Le nombre de fois à appeler wait_n.
        max_delay (int): Le délai maximum pour chaque appel à wait_n.

    Returns:
        float: Le temps moyen d'exécution par appel à wait_n.
    """
    async def async_measure():
        """A asynchronous function"""
        start_time = time.time()  # Enregistre le temps de départ

        await wait_n(n, max_delay)

        end_time = time.time()  # Enregistre le temps de fin
        total_time = end_time - start_time
        # Calcule le temps total d'exécution

        return (total_time) / n  # Calcule le temps moyen par appel

    return asyncio.run(async_measure())
