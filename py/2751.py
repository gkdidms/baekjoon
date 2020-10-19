import heapq
import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    m = int(sys.stdin.readline())
    heapq.heappush(li,m)

for _ in range(n):
    print(heapq.heappop(li))