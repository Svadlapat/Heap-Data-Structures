"""
scheduler.py
-------------
Simple scheduler simulation using BinaryHeapPQ.
Two policies supported:
- "max_priority": use a max-heap over Task.priority
- "earliest_deadline": use a min-heap over Task.deadline (ties broken by higher priority)

Run this file directly to see a small demo.
"""

from typing import List, Optional
from dataclasses import dataclass
from priority_queue import BinaryHeapPQ, Task

@dataclass
class Result:
    completed: List[Task]
    missed_deadlines: int
    total_time: int
    average_wait: float

def simulate(tasks: List[Task], policy: str = "max_priority") -> Result:
    time_now = 0
    completed: List[Task] = []
    missed = 0

    if policy == "max_priority":
        pq = BinaryHeapPQ(mode="max")
    elif policy == "earliest_deadline":
        # We'll reuse Task.priority as the ordering key by setting it to the deadline.
        pq = BinaryHeapPQ(mode="min")
    else:
        raise ValueError("policy must be 'max_priority' or 'earliest_deadline'")

    # Sort by arrival
    tasks_sorted = sorted(tasks, key=lambda t: t.arrival_time)
    i = 0
    wait_times = []

    while i < len(tasks_sorted) or not pq.is_empty():
        # Add arrived tasks
        while i < len(tasks_sorted) and tasks_sorted[i].arrival_time <= time_now:
            t = tasks_sorted[i]
            t.meta = t.meta or {}
            if policy == "earliest_deadline":
                if t.deadline is None:
                    raise ValueError("earliest_deadline policy requires deadlines on tasks")
                # For min-heap, lower 'priority' is better. Use deadline primarily.
                # Store original priority for reference.
                t.meta["orig_priority"] = t.priority
                t.priority = float(t.deadline)
            pq.insert(t)
            i += 1

        if pq.is_empty():
            # Fast-forward to next arrival
            time_now = tasks_sorted[i].arrival_time
            continue

        current = pq.extract()
        start_time = time_now
        time_now += current.duration
        finish_time = time_now

        # Check deadline (if exists)
        if current.deadline is not None and finish_time > current.deadline:
            missed += 1

        # Wait time = start - arrival
        wait_times.append(start_time - current.arrival_time)
        completed.append(current)

    avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0.0
    return Result(completed=completed, missed_deadlines=missed, total_time=time_now, average_wait=avg_wait)

if __name__ == "__main__":
    # Demo
    demo_tasks = [
        Task(task_id="A", priority=5, arrival_time=0, deadline=8, duration=3),
        Task(task_id="B", priority=1, arrival_time=1, deadline=7, duration=2),
        Task(task_id="C", priority=10, arrival_time=2, deadline=12, duration=4),
        Task(task_id="D", priority=7, arrival_time=6, deadline=14, duration=3),
    ]
    print("Max-Priority policy:")
    res1 = simulate([t for t in demo_tasks], policy="max_priority")
    print("Completed order:", [t.task_id for t in res1.completed])
    print("Missed deadlines:", res1.missed_deadlines, "Total time:", res1.total_time, "Avg wait:", round(res1.average_wait, 2))

    print("\nEarliest Deadline First policy:")
    res2 = simulate([t for t in demo_tasks], policy="earliest_deadline")
    print("Completed order:", [t.task_id for t in res2.completed])
    print("Missed deadlines:", res2.missed_deadlines, "Total time:", res2.total_time, "Avg wait:", round(res2.average_wait, 2))
