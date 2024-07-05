#!/usr/bin/env python3
"""
safe_first_element

"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element
    """
    if lst:
        return lst[0]
    else:
        return None
