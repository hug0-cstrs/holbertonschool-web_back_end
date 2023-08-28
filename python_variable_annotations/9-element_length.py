#!/usr/bin/env python3""
"""A type annotated simple function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a sequence and int inside a tuple that inside a list"""
    return [(i, len(i)) for i in lst]
