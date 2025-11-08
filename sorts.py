"""
sorts.py
---------
Reference implementations for Randomized Quicksort and Merge Sort used for empirical comparison
with Heapsort.
"""

import random
from typing import List, Callable, Optional, TypeVar

T = TypeVar("T")

def randomized_quicksort(a: List[T], key: Optional[Callable[[T], T]] = None) -> List[T]:
    if key is None:
        key = lambda x: x

    def _qs(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        pivot_index = random.randint(lo, hi)
        a[hi], a[pivot_index] = a[pivot_index], a[hi]
        pivot = key(a[hi])
        i = lo
        for j in range(lo, hi):
            if key(a[j]) <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        _qs(lo, i - 1)
        _qs(i + 1, hi)

    _qs(0, len(a) - 1)
    return a

def mergesort(a: List[T], key: Optional[Callable[[T], T]] = None) -> List[T]:
    if key is None:
        key = lambda x: x

    def _ms(arr: List[T]) -> List[T]:
        n = len(arr)
        if n <= 1:
            return arr
        mid = n // 2
        left = _ms(arr[:mid])
        right = _ms(arr[mid:])
        return _merge(left, right)

    def _merge(left: List[T], right: List[T]) -> List[T]:
        i = j = 0
        out: List[T] = []
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
        out.extend(left[i:]); out.extend(right[j:])
        return out

    res = _ms(list(a))
    a[:] = res
    return a
