#!/usr/bin/env python3
"""Run time for 4 parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that will execute async_comprehension four times in
        parallel using asyncio.gather."""
    time1 = time.perf_counter()
    asyncio.gather(async_comprehension(),
                   async_comprehension(),
                   async_comprehension(),
                   async_comprehension())
    time2 = time.perf_counter()
    return time2 - time1
