"""
benchmarks.py
--------------
Empirically compare Heapsort, Randomized Quicksort, and Merge Sort across input sizes and distributions.
Writes results to benchmarks.csv and a short Markdown summary.
"""

import time, random, csv, statistics
from typing import List, Callable
from heapsort import heapsort
from sorts import randomized_quicksort, mergesort

def make_data(n: int, dist: str) -> List[int]:
    if dist == "random":
        return [random.randint(0, 10**6) for _ in range(n)]
    elif dist == "sorted":
        return list(range(n))
    elif dist == "reverse":
        return list(range(n, 0, -1))
    else:
        raise ValueError("unknown distribution")

def time_algo(fn: Callable[[List[int]], List[int]], data: List[int], repeats: int = 3) -> float:
    times = []
    for _ in range(repeats):
        arr = list(data)
        t0 = time.perf_counter()
        fn(arr)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.median(times)

def run():
    sizes = [2000, 5000, 10000]  # adjust as needed
    dists = ["random", "sorted", "reverse"]
    algos = [
        ("Heapsort", heapsort),
        ("RandomizedQuicksort", randomized_quicksort),
        ("MergeSort", mergesort),
    ]
    rows = []
    for n in sizes:
        for dist in dists:
            base = make_data(n, dist)
            for name, fn in algos:
                elapsed = time_algo(fn, base, repeats=3)
                rows.append({"n": n, "distribution": dist, "algorithm": name, "seconds": elapsed})
                print(f"{name:20s} n={n:6d} dist={dist:8s} -> {elapsed:.6f}s")

    with open("benchmarks.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["n","distribution","algorithm","seconds"])
        writer.writeheader()
        writer.writerows(rows)

    # Simple markdown summary
    by_key = {}
    for r in rows:
        key = (r["n"], r["distribution"])
        by_key.setdefault(key, []).append((r["algorithm"], r["seconds"]))

    lines = ["# Benchmark Summary\n"]
    for (n, dist), items in sorted(by_key.items()):
        lines.append(f"## n={n}, distribution={dist}\n")
        for name, sec in sorted(items, key=lambda x: x[1]):
            lines.append(f"- {name}: {sec:.6f} s")
        lines.append("")
    with open("benchmark_summary.md", "w") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    run()
