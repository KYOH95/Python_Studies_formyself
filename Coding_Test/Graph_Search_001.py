#1260
#DFS와 BFS
import sys
si = sys.stdin.readline
from collections import deque

N,M,V = list(map(int,si().split()))
adj = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = list(map(int,si().split()))
    adj[x].append(y)
    adj[y].append(x)

for i in range(1,N+1):
    adj[i].sort()

def DFS(x):
    visited[x] = 1
    print(x,end=' ')
    for cand in adj[x]:
        if visited[cand]==1: continue
        DFS(cand)

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        print(x,end=" ")
        for y in adj[x]:
            if visited[y]: continue
            visited[y]=1
            queue.append(y)

visited = [0] * (N+1)
DFS(V)
print()
visited = [0] * (N+1)
BFS(V)
