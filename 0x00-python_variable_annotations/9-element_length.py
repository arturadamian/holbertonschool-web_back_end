#!/usr/bin/env python3
""" Let's duck type an iterable object
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate this function’s parameters
        and return values with the appropriate types
        Args:
            lst: Iterable[Sequence]
        Returns: List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
