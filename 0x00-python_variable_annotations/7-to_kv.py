#!/usr/bin/env python3
'''
a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))
