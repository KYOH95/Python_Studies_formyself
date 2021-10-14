#11725
#트리의 부모 찾기

import sys
from collections import deque
sys.setrecursionlimit(10000)
si = sys.stdin.readline

N = int(si())
lines = [[]for _ in range(N+1)]
for i in range(N-1):
    x,y = map(int,si().split())
    lines[x].append(y)
    lines[y].append(x)

parent = [0 for _ in range(N+1)]
def BFS(x):
    visited = [False for _ in range(N+1)]
    visited[x] = True
    queue = deque()
    queue.append(x)    
    while(queue):
        x = queue.popleft()
        for y in lines[x]:
            if visited[y]: continue
            visited[y]= True
            queue.append(y)
            parent[y] = x

BFS(1)
    
for i in range(2,N+1):
    print(parent[i])