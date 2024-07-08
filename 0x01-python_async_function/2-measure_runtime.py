#!/usr/bin/env python3
"""
elapsed time
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    elapsed time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed = end - start
    result = elapsed / n
    return result
