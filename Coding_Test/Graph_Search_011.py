#boj_7562
#knight

import sys
from collections import deque
si = sys.stdin.readline


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
        
    print(dist[goal[0]][goal[1]])


T = int(si())

for i in range(T):
    N = int(si()) 
    start = list(map(int,si().split()))
    goal = list(map(int,si().split()))
    bfs(start[0],start[1])

