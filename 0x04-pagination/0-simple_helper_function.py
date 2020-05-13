#!/usr/bin/env pyhton3
"""return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
"""


def index_range(page, page_size):
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = page_size * page
    return (start_index, end_index)
