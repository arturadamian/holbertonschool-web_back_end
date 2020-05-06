#!/usr/bin/env python3
"""The basics of async - Tasks
"""
import asyncio
import bisect
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    list_of_delays: List[float] = []
    for _ in range(n):
        bisect.insort(list_of_delays, await task_wait_random(max_delay))
    return list_of_delays
