#!/usr/bin/env python3
"""
Multiple coroutines at the same time with async
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine called wait_n that takes in 2 int arguments: n and
       max_delay. You will spawn wait_random n times with the specified
       max_delay.wait_n return the list of all the delays (float values)"""
    lista = []
    for i in range(n):
        num = await wait_random(max_delay)
        lista.append(num)
    return sorted(lista)
