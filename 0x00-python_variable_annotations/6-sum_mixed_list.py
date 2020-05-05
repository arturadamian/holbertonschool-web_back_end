#!/usr/bin/env python3
""" Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ returns the sum of elements of the list as a float.
        Args:
            mxd_lst: List[Union[float, int]]
        Returns: float
    """
    return sum(mxd_lst)
