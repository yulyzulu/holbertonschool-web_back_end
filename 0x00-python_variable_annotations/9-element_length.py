#!/usr/bin/env python3
"""Iterable object"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence[int]]]:
    return [(i, len(i)) for i in lst]
