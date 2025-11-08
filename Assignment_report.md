Assignment 4: Heap Data Structures — Implementation, Analysis, and Applications  
 


1. Introduction

This report explores heap data structures, their implementation using arrays,
their role in the Heapsort algorithm, and their use in priority queues and
scheduler systems. The assignment has two major parts:

1. Heapsort implementation, analysis, and comparison with other sorting algorithms.
2. Priority queue implementation using binary heaps and its use in a scheduling simulation.


2. Heapsort Implementation

Heapsort is an in-place, comparison-based sorting algorithm that uses a binary
max-heap. The algorithm consists of two steps:

1. Build a max heap from the array.
2. Repeatedly remove the largest element from the heap and place it at the end.

No recursion is needed, and the array itself acts as the heap structure.


3. Time Complexity Analysis

| Phase               | Time Complexity |
|---------------------|-----------------|
| Build Max Heap      | Θ(n)            |
| Extract Max (n−1x)  | Θ(log n) each   |
| Total Time          | Θ(n log n)      |

Heapsort always performs n extractions, and each extraction costs log n,
therefore the total complexity is Θ(n log n) in worst, average, and best cases.


4. Why Heapsort Is Θ(n log n) in All Cases

Unlike Quicksort, Heapsort does not depend on pivot choice or input order.
The cost of sifting down is always bounded by the height of the heap (log n),
which does not change based on the initial order of elements.

Therefore, even the best case cannot go below n log n.


5. Space Complexity

Heapsort is an in-place algorithm:

| Component              | Space |
|------------------------|-------|
| Array / Heap           | O(n)  |
| Extra Variables        | O(1)  |
| Total Extra Space      | O(1)  |

This makes it more memory-efficient than Merge Sort (O(n) extra space).


6. Empirical Comparison with Other Algorithms

Algorithms tested: Heapsort, Randomized Quicksort, Merge Sort  
Input sizes: 2000, 5000, 10000  
Distributions: Random, Sorted, Reverse Sorted

Example results:

n = 2000 (random)
- Randomized Quicksort: 0.00458 s
- Merge Sort: 0.00560 s
- Heapsort: 0.00729 s

n = 10000 (reverse)
- Merge Sort: 0.02390 s
- Randomized Quicksort: 0.02528 s
- Heapsort: 0.04386 s

Observations:
- Merge Sort is the fastest in most cases due to cache locality.
- Quicksort performs well on random data but can degrade if pivot is bad.
- Heapsort is the slowest in practice but most predictable in runtime.

=
7. Priority Queue Implementation

The priority queue is implemented using a binary heap. Supported operations:

| Operation              | Time |
|------------------------|------|
| insert(task)           | O(log n) |
| extract_max/min()      | O(log n) |
| increase/decrease_key  | O(log n) |
| is_empty()             | O(1) |

The priority queue supports both:
- Max-Heap mode (highest priority first)
- Min-Heap mode (lowest value / earliest deadline first)


8. Scheduler Simulation

Two CPU scheduling strategies implemented:

| Policy                 | Heap Type | Use Case      |
|------------------------|-----------|---------------|
| Highest Priority First | Max-Heap  | OS schedulers |
| Earliest Deadline First| Min-Heap  | Real-time systems |

Metrics Recorded:
- Order of execution
- Number of missed deadlines
- Average waiting time
- Total completion time


9. Real-World Applications of Heaps

 Operating System CPU scheduling  
 Packet scheduling in routers (QoS)  
 A* pathfinding (open set priority queue)  
 Discrete event simulation engines  
 Huffman coding tree generation  
 Dijkstra’s shortest path algorithm  
 k-largest / k-smallest selection queries  


10. Conclusion

Heapsort guarantees Θ(n log n) runtime and O(1) extra memory, making it
theoretically optimal. However, in real execution it is slower than Quicksort
and Merge Sort due to poor cache performance.

Binary heaps provide the foundation for efficient priority queues, which are
critical to schedulers in operating systems, networking, databases, and AI.

