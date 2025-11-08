"""
heapsort.py
------------
Clean, well-documented implementation of Heapsort using an array-based max-heap.
Includes helper functions: sift_down, build_max_heap, and heapsort.
"""

from typing import List, Callable, Optional, TypeVar

T = TypeVar("T")

def sift_down(a: List[T], start: int, end: int, key: Optional[Callable[[T], T]] = None) -> None:
    """
    Restore the max-heap property by sifting the element at index `start` down to its correct position
    within the subarray a[start:end]. The subarray is treated as a heap rooted at `start`.
    """
    if key is None:
        key = lambda x: x  # identity
    
    root = start
    while True:
        left = 2 * root + 1
        right = left + 1
        largest = root

        if left < end and key(a[left]) > key(a[largest]):
            largest = left
        if right < end and key(a[right]) > key(a[largest]):
            largest = right

        if largest == root:
            return
        a[root], a[largest] = a[largest], a[root]
        root = largest

def build_max_heap(a: List[T], key: Optional[Callable[[T], T]] = None) -> None:
    """
    In-place bottom-up heap construction in O(n) time.
    """
    n = len(a)
    # Start from the last parent and sift down
    for i in range((n // 2) - 1, -1, -1):
        sift_down(a, i, n, key=key)

def heapsort(a: List[T], key: Optional[Callable[[T], T]] = None) -> List[T]:
    """
    In-place Heapsort. Returns the same list reference sorted in ascending order (based on key).
    Time Complexity: O(n log n) in worst, average, and best cases.
    Space Complexity: O(1) auxiliary (in-place).
    """
    if key is None:
        key = lambda x: x
    n = len(a)
    build_max_heap(a, key=key)
    # Repeatedly move max to the end and restore heap
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end, key=key)
    return a

if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Original:", data)
    heapsort(data)
    print("Sorted:", data)
