#!/usr/bin/env python3
"""Complex types"""

from typing import Callable



def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float multiplier
     as argument and returns a function that multiplies a float by multiplier."""

    def fun_multiplier(n: float) -> float:
        """Multiplication function"""
        return float(n * multiplier)

    return fun_multiplier
