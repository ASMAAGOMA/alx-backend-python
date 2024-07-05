#!/usr/bin/env python3
"""
return fun
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    retrun fun
    """
    def mul(x: float) -> float:
        return multiplier * x
    return mul
