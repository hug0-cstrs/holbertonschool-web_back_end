#!/usr/bin/env python3""
"""A type annotated simple function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns another function that multiplies
    x by the passed variable
    """
    def x(f: float) -> float:
        """a Callable function that returns a float"""
        return float(f * multiplier)
    return x
