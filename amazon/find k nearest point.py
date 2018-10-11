# In Python, the priority queue function is the heapq, also known as the priority queue algo

# Heaps are binary trees for which every parent node has a value less than equal than the children

# so the ROOT is the Smallest, heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,

# In python, the suggested way that is the heap elements could be tuple

def heapsort(iterable):
    h = []
    for v in iterable:
        heapq.heappush(h, v)
    return [heapq.heappop() for i in range(len(h))]



import heapq
import math


def get_distance(p1, p2):
    return math.sqrt(  (p1.x - p2.x)**2  + (p1.y - p2.y)**2  )

# since we hava an origin, so the value should be the same


def k_nearest_point(points, origin, k):
    res = []
    index = 0

    pq = []

    for point in points:
        heapq.heappush(pq, (get_distance(points, origin), point))

        if len(pq) > k:
            heapq.heappop(pq)

    while pq:
        res[index] = heapq.heappop(pq)[1]
        index += 1

    return res
