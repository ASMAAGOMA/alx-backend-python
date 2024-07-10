#!/usr/bin/env python3
"""
async loop
"""


from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    result = [i async for i in async_generator()]
    return result
