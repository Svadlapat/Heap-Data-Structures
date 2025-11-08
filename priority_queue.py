"""
priority_queue.py
------------------
Binary Heap based Priority Queue supporting:
- insert(task)
- extract_max() / extract_min()
- increase_key(task_id, new_priority) / decrease_key(task_id, new_priority)
- is_empty()

Uses an array-based heap and an index map for O(log n) key updates by task_id.

Choose min-heap or max-heap by setting `mode` = "min" or "max".
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(order=True)
class Task:
    """
    Represents a schedulable task.
    Comparable by priority (for heap ordering) but we keep an explicit mode to flip comparison.
    """
    priority: float
    task_id: str
    arrival_time: int = 0
    deadline: Optional[int] = None
    duration: int = 1
    meta: Optional[dict] = None

class BinaryHeapPQ:
    """
    Array-based Binary Heap Priority Queue with O(log n) insert/extract and key updates.
    mode = "max" -> highest priority first
    mode = "min" -> lowest priority first
    """
    def __init__(self, mode: str = "max") -> None:
        assert mode in ("min", "max"), "mode must be 'min' or 'max'"
        self.mode = mode
        self._heap: List[Task] = []
        self._pos: Dict[str, int] = {}   # task_id -> index in heap array

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    # --- helpers ---
    def _better(self, a: Task, b: Task) -> bool:
        return a.priority < b.priority if self.mode == "min" else a.priority > b.priority

    def _swap(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._pos[self._heap[i].task_id] = i
        self._pos[self._heap[j].task_id] = j

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._better(self._heap[idx], self._heap[parent]):
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        n = len(self._heap)
        while True:
            left = 2 * idx + 1
            right = left + 1
            best = idx
            if left < n and self._better(self._heap[left], self._heap[best]):
                best = left
            if right < n and self._better(self._heap[right], self._heap[best]):
                best = right
            if best == idx:
                break
            self._swap(idx, best)
            idx = best

    # --- core operations ---
    def insert(self, task: Task) -> None:
        if task.task_id in self._pos:
            raise ValueError(f"Task with id '{task.task_id}' already present")
        self._heap.append(task)
        idx = len(self._heap) - 1
        self._pos[task.task_id] = idx
        self._sift_up(idx)

    def peek(self) -> Optional[Task]:
        return self._heap[0] if self._heap else None

    def extract(self) -> Task:
        if not self._heap:
            raise IndexError("extract from empty priority queue")
        self._swap(0, len(self._heap) - 1)
        top = self._heap.pop()
        del self._pos[top.task_id]
        if self._heap:
            self._sift_down(0)
        return top

    def extract_max(self) -> Task:
        if self.mode != "max":
            raise RuntimeError("Priority queue is not a max-heap")
        return self.extract()

    def extract_min(self) -> Task:
        if self.mode != "min":
            raise RuntimeError("Priority queue is not a min-heap")
        return self.extract()

    def increase_key(self, task_id: str, new_priority: float) -> None:
        if task_id not in self._pos:
            raise KeyError(f"task_id '{task_id}' not found")
        idx = self._pos[task_id]
        if new_priority <= self._heap[idx].priority:
            raise ValueError("new_priority must be greater than current priority for increase_key")
        self._heap[idx].priority = new_priority
        if self.mode == "max":
            self._sift_up(idx)
        else:
            # In a min-heap, increasing a key may require sifting down
            self._sift_down(idx)

    def decrease_key(self, task_id: str, new_priority: float) -> None:
        if task_id not in self._pos:
            raise KeyError(f"task_id '{task_id}' not found")
        idx = self._pos[task_id]
        if new_priority >= self._heap[idx].priority:
            raise ValueError("new_priority must be less than current priority for decrease_key")
        self._heap[idx].priority = new_priority
        if self.mode == "min":
            self._sift_up(idx)
        else:
            # In a max-heap, decreasing a key may require sifting down
            self._sift_down(idx)
