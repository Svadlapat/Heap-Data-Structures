# Assignment 4: Heap Data Structures — Implementation, Analysis, and Applications

**Author:** Your Name  
**Date:** 8 November 2025

## Overview
This report presents:
1. A clear, efficient implementation of **Heapsort** using an array-based max-heap.
2. A rigorous **time and space analysis** for Heapsort.
3. An **empirical comparison** of Heapsort vs **Randomized Quicksort** and **Merge Sort** over various input sizes and distributions.
4. A **Priority Queue** implemented using an array-based binary heap with core operations (`insert`, `extract_max/min`, `increase/decrease_key`, `is_empty`).
5. A small **scheduler simulation** that uses the priority queue in two modes: highest-priority-first and earliest-deadline-first (EDF).

---

## Heapsort Implementation
- File: `heapsort.py`
- Core functions: `sift_down`, `build_max_heap`, `heapsort`  
- In-place, iterative heap maintenance (no recursion) for predictable space usage.

### Correctness Sketch
1. **Heap construction** ensures parent ≥ children (max-heap).  
2. The maximum element at the root is repeatedly swapped with the end of the array and removed from the heap region.  
3. **Sift-down** restores the heap invariant after each extraction.  
4. The suffix grows sorted in ascending order while the prefix remains a valid heap, terminating with a fully sorted array.

## Heapsort Complexity Analysis
- **Worst / Average / Best Time:** Θ(n log n).  
  - Building the heap is Θ(n).  
  - Each of the n−1 extractions performs at most `⌊log n⌋` swaps/sifts → Θ(n log n) overall.
- **Why O(n log n) in all cases?**  
  Heapsort always performs n−1 extractions and each extraction requires re-heapification bounded by the tree height `O(log n)` independent of input order. There is no best-case shortcut like in Quicksort (which can hit O(n²) on adversarial input). Hence the bound remains **Θ(n log n)** uniformly.
- **Space Complexity:** O(1) auxiliary.  
  Sorting is performed in-place; only a constant number of indices and temporaries are used. (Recursive variants would add stack overhead, but our implementation is iterative.)

**Overheads:** Cache locality is poorer than mergesort/quicksort due to non-sequential access during sifts; constant factors may be higher even though the asymptotic complexity is optimal.

---

## Empirical Comparison
We compare **Heapsort**, **Randomized Quicksort**, and **Merge Sort** across sizes `{2000, 5000, 10000}` and distributions `{random, sorted, reverse}`.  
Code: `benchmarks.py` (uses our in-repo implementations).

### Environment
- Python 3 (no external libraries)  
- Timing via `time.perf_counter()`; median of 3 runs per (size, distribution, algorithm).

### Execution:
``` bash
python heapshort.py

python scheduler.py

python benchmarks.py
```

### Results (example snapshot)
A CSV (`benchmarks.csv`) and a Markdown summary (`benchmark_summary.md`) are produced. 

