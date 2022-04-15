#DFS와 BFS
#link: https://www.acmicpc.net/problem/1260

import sys
from collections import deque
si = sys.stdin.readline

N,M,V = list(map(int,si().split()))
g = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = list(map(int,si().split()))
    g[a].append(b)
    g[b].append(a)

for i in range(1,N+1):
    g[i].sort()

dfs_check = [0] * (N+1)
def dfs(start):
    dfs_check[start] = 1
    print(start,end=" ")
    for x in g[start]:
        if dfs_check[x] == 1: continue
        dfs(x)

bfs_check = [0] * (N+1)
def bfs(start):
    queue = deque()
    queue.append(start)
    bfs_check[start] = 1
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for y in g[x]:
            if bfs_check[y] == 1: continue
            bfs_check[y] = 1
            queue.append(y)

dfs(V)
print()
bfs(V)
