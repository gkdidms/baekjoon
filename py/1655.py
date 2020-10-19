import heapq
import sys
N = int(sys.stdin.readline())
maxheap = []
minheap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, (-n,n))
    else:
        heapq.heappush(minheap, (n,n))

    if minheap and maxheap[0][1] > minheap[0][1]:
        max_value = heapq.heappop(maxheap)[1]
        min_value = heapq.heappop(minheap)[1]
        heapq.heappush(min_value, (max_value,max_value))
        heapq.heappush(max_value, (-min_value,min_value))
    
    print(maxheap[0][1])