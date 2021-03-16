#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the total execution time for
       wait_n(n, max_delay), and returns total_time / n"""
    time1 = time.perf_counter()
    wait_n(n, max_delay)
    time2 = time.perf_counter()
    return time2 - time1
