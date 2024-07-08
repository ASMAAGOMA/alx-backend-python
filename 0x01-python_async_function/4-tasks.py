#!/usr/bin/env python3
"""
several random waits
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    several awaits
    """
    awaits = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    final = []
    for one in awaits:
        final.append(one)
        for i in range(len(final) - 1, 0, -1):
            if (final[i] < final[i - 1]):
                final[i], final[i - 1] = final[i - 1], final[i]
            else:
                break
    return final
