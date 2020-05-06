#!/usr/bin/env python3
""" Let's execute multiple coroutines
    at the same time with async
"""
import bisect
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    # return the list of all the delays in ascending order
    list_of_delays = []
    for _ in range(n):
        bisect.insort(list_of_delays, await wait_random(max_delay))
    return list_of_delays
