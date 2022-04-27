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
    v_check[start] = True
    while Q:
        x = Q.popleft()
        for y in network[x]:
            if v_check[y] == True: continue
            v_check[y] == True
            Q.append(y)

count = 0
for x in v_check:
    if x == True:
        count += 1

bfs(1)
print(count)
