#boj_18404
#현명한 나이트

import sys
from collections import deque
si = sys.stdin.readline

N,M = map(int,si().split()) 
a,b = map(int,si().split())
start = [a-1,b-1]
goal = [[]for _ in range(M)]
for i in range(M): 
    a,b = map(int,si().split())
    goal[i] = [a-1,b-1]


def bfs(x,y):
    dist = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    dir = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]
    visited[x][y]=True
    queue = deque()
    queue.append(x)
    queue.append(y)

    while queue:
        x = queue.popleft()
        y = queue.popleft()

        for dx,dy in dir:
            nx = dx + x
            ny = dy + y
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny]: continue
            dist[nx][ny] = dist[x][y] + 1
            visited[nx][ny] = True
            queue.append(nx)
            queue.append(ny)
        
    for i in range(M):
        print(dist[goal[i][0]][goal[i][1]],end=' ')
    
bfs(start[0],start[1])
