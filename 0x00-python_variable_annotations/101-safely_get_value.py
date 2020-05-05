#!/usr/bin/env python3
""" More involved type annotations
"""
from typing import Union, Mapping, Any, TypeVar
T = TypeVar('T')


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[T, None]=None
            ) -> Union[Any, T]:
    """
        add type annotations to the function
        Args:
            dct: Mapping
            key: Any
            default: Union[T, None] = None)
        Returns: Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
