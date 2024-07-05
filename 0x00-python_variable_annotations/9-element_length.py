#!/usr/bin/env python3
"""
element len
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
