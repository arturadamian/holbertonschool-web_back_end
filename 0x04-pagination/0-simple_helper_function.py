#!/usr/bin/env pyhton3
"""return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page and page_size:
        start_index: int = (page - 1) * page_size
        end_index: int = start_index + page_size
    return (start_index, end_index)
