#!/usr/bin/env python3
""" From the previous file, import wait_n into 2-measure_runtime.py"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
