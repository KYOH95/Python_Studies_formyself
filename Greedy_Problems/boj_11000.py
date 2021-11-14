#boj_11000
#강의실 배정

import sys
import heapq
si = sys.stdin.readline

N = int(si())
list_ = [list(map(int,si().split())) for _ in range(N)]

list_ = sorted(list_,key = lambda x:x[0])

q = []

for x in list_:
    if not q:
        pass
    elif q and q[0] <= x[0]:
        heapq.heappop(q)
    heapq.heappush(q,x[1])

print(q)
print(len(q))


