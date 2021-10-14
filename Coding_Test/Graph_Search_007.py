#2606
#바이러스

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

C = int(si())
Lines = int(si())
a = [[] for _ in range(C+1)]
for _ in range(1,Lines+1):
    x,y = map(int,si().split())
    a[x].append(y)
    a[y].append(x)

def DFS(x):
    visited[x] = True
    for cand in a[x]:
        if visited[cand]: continue
        visited[cand] = True
        DFS(cand)

visited = [False for _ in range(C+1)]
DFS(1)
count = -1
for x in visited:
    if x == True: count += 1

print(count)