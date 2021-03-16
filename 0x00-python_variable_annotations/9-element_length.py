#!/usr/bin/env python3
"""Iterable object"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below functions parameters and return values with the
        appropriate types"""
    return [(i, len(i)) for i in lst]
