#!/usr/bin/env python3
"""a function task_wait_random"""


from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    ''' task wait randomthat takes an integer
    max_delay and returns a asyncio.Task'''
    task = create_task(wait_random(max_delay))
    return task
