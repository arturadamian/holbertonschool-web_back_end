#!/usr/bin/env python3
"""  Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of elements of the list as a float.
        Args:
            input_list: List[float]
        Returns: float
    """
    return sum(input_list)
