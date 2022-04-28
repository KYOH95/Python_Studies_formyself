#바이러스
#Link: https://www.acmicpc.net/problem/2606

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

C = int(si())
N = int(si())
network = [[] for _ in range(C+1)]

for _ in range(N):
    x,y = list(map(int,si().split()))
    network[x].append(y)
    network[y].append(x)

v_check = [False] * (C+1)
def bfs(start):
    Q = deque()
    Q.append(start)
    v_check[start] = 1
    while Q:
        x = Q.popleft()
        for y in network[x]:
            if v_check[y]: continue
            v_check[y] = True
            Q.append(y)


bfs(1)
count = -1
for x in v_check:
    if x: count += 1
print(count)
