#!/usr/bin/env python3
"""
several random waits
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    several awaits
    """
    awaits = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    final = []
    for one in awaits:
        final.append(one)
        for i in range(len(final) - 1, 0, -1):
            if (final[i] < final[i - 1]):
                final[i], final[i - 1] = final[i - 1], final[i]
            else:
                break
    return final
