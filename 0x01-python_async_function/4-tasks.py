#!/usr/bin/env python3
"""
Task Function
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine called wait_n that takes in 2 int arguments: n and
       max_delay. You will spawn wait_random n times with the specified
       max_delay.wait_n return the list of all the delays (float values)"""
    lista = []
    for i in range(n):
        num = await task_wait_random(max_delay)
        lista.append(num)
    return sorted(lista)
